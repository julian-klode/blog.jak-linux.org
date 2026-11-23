---
title: "Introducing apt-core-json"
date: 2026-11-23T18:20:49+01:00
---

Today I finalized apt-core-json, the first in a new set of core libraries for APT to bring APT into the new decade,
following the latest C++23 standard, with a focus on memory safety, absurd amounts of template metaprogramming,
and of course: coroutines and event loops, leading to a Varlink library as the next big deliverable.
The running joke is that the "Core" stands for "*Cor*outines and *E*vent Loop".

The JSON library was one of the first things needed for a Varlink library.
JSON is not particularly hard,
but I did not want to write my own parser (and I deleted my old writer!).
Instead of a custom library, I had to pick json-c as the backend.
I then had to work around a whole ton of issues with json-c not being strict enough;
heck that thing will read embedded NUL bytes in strings and then silently truncate them!
So we had to implement a verification step that understands enough JSON to reject
"\u0000" as well as literal NUL bytes in input strings.
In an optimal world, I'd just use sd-varlink, but obviously it's not available on Hurd.

This work just landed in main, and I want to share with you the concepts of the library.

## Core types
APT::JSON provides two main types:

- View, which is a read-only view into a JSON object
- Value, which is an owned, move-only, mutable reference

Let's have a look at how this plays out decoding a Varlink call:

```c++
auto val = JSON::Value::parse(someString);
if (not val)
    return std::unexpected(val.error());
auto call = val.get<Call>();
if (not call)
    return std::unexpected(call.error());

std::cerr << "Called with method: " << call->method << "\n";
std::cerr << "              more: " << call->more << "\n";

auto backIntoJson = JSON::Value::encode(call);
if (not backIntoJson)
    return std::unexpected(backIntoJson.error());
```

You may notice the `get<Call>()` syntax and the `encode`
call. These are implemented using `Encode` and `Decode`
templates.

## Encoders and Decoders

Encoders and decoders are relatively straightforward;
instantiate the `Encode` and/or `Decode` template for
the type you want to make encodable, and you are done:


```c++
struct TestStruct
{
   std::string name;
   std::optional<int> count;
};

template <>
struct JSON::Decode<TestStruct>
{
   static std::expected<TestStruct, JSON::Error> operator()(JSON::View v)
   {
      TestStruct result;
      return v.into("name", result.name)
         .and_then([&] noexcept { return v.into("count", result.count); })
         .transform([&] { return result; });
   }
};

static_assert(JSON::Decodable<TestStruct>);

template <>
struct JSON::Encode<TestStruct>
{
   static std::expected<Value, JSON::Error> operator()(const TestStruct &val)
   {
      auto obj = Value::object();
      return obj.set("name", val.name)
         .and_then([&] { return obj.set("count", val.count); })
         .transform([&] { return std::move(obj); });
   }
};
```
Doing this a bunch of times gets old quickly, so of course we added
reflection.

## Reflection

Reflection allows you to inspect the fields a class has and how they
map to JSON keys. Doing so is quite straightforward:

```c++
struct ReflectableTestStruct
{
   std::string name;
   std::optional<int> count;
};

template <>
struct JSON::Reflect<ReflectableTestStruct>
{
   static constexpr auto operator()(auto &val) noexcept
   {
      return std::tuple{
         std::pair{"name", std::ref(val.name)},
         std::pair{"count", std::ref(val.count)},
      };
   }
};
```

But this also gets a bit repetitive so if you want you can use
a macro:

```c++
APT_REFLECT(ReflectableTestStruct, APT_FIELD(name), APT_FIELD(count));
```

The `APT_FIELD` macro also takes an optional second argument (a
string) to specify the name in the JSON object.

One thing to point out is that reflection handles missing fields and null values the same:
A `std::nullopt` is skipped during Encode, and missing fields or `null` values yield `nullopt` equally.

## What's next?

The next step is likely `apt-core-io`,
which implements an `EventLoop` and `FileDescriptor` utilizing the coroutine features from recent C++ standard versions.

Then we can implement `APT::Varlink::Server` and `APT::Varlink::Client`
on top of this.

The aim is for `APT::Varlink` to likewise be self-describing; a method
should have a `MethodSpec` and an interface an `InterfaceSpec`, and
the IDL should be automatically generated from it, as well as the
dispatch to the coroutines handling responses.

This will allow us to have a fully type-safe Varlink implementation
with incredible ergonomics.


