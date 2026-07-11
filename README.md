# @me-id/protos

[![npm](https://img.shields.io/npm/v/@me-id/protos?label=npm&color=2563eb)](https://www.npmjs.com/package/@me-id/protos)
[![GitHub release](https://img.shields.io/github/v/release/me-id/protos?label=release&color=059669)](https://github.com/me-id/protos/releases)
[![License](https://img.shields.io/badge/license-Apache--2.0-2563eb)](LICENSE)
[![TypeScript](https://img.shields.io/badge/types-TypeScript-3178c6)](gen/es/meid/did/v1/did_pb.ts)
[![Protocol Buffers](https://img.shields.io/badge/protobuf-Buf-0c66e4)](buf.yaml)

> **Official protobuf definitions for the did:me identity method**, including:
>
> - DID Documents  
> - Verification Methods  
> - Services  
> - Update Policies  
> - Domain Verification  
> - Attestations  
> - Data Integrity Proofs  
>
> Generated with **Buf**, with checked-in outputs for TypeScript,
> JavaScript, Go, Rust, Swift, Kotlin, and Python. Algorithm fields import the
> shared `reallyme.crypto.v1` contract from `reallyme/crypto/v1/crypto.proto`;
> Kotlin and Java generated types use `me.really.crypto.v1`, matching the
> `me.really:crypto` Maven package.

---

## Import

~~~ts
import { CoreKeySchema } from "@me-id/protos/did/v1";
~~~

The package exports the did:me schema surface. Generated crypto descriptor files
are included so the DID modules resolve their `reallyme.crypto.v1` imports;
application code that needs crypto operations should use `@reallyme/crypto` or
`me.really:crypto` directly.

## Install

~~~
npm install @me-id/protos
~~~

~~~
pnpm add @me-id/protos
~~~

~~~
yarn add @me-id/protos
~~~
