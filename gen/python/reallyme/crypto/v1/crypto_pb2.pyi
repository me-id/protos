from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CryptoAlgorithmFamily(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CRYPTO_ALGORITHM_FAMILY_UNSPECIFIED: _ClassVar[CryptoAlgorithmFamily]
    CRYPTO_ALGORITHM_FAMILY_SIGNATURE: _ClassVar[CryptoAlgorithmFamily]
    CRYPTO_ALGORITHM_FAMILY_KEY_AGREEMENT: _ClassVar[CryptoAlgorithmFamily]
    CRYPTO_ALGORITHM_FAMILY_KEM: _ClassVar[CryptoAlgorithmFamily]
    CRYPTO_ALGORITHM_FAMILY_AEAD: _ClassVar[CryptoAlgorithmFamily]
    CRYPTO_ALGORITHM_FAMILY_HASH: _ClassVar[CryptoAlgorithmFamily]
    CRYPTO_ALGORITHM_FAMILY_MAC: _ClassVar[CryptoAlgorithmFamily]
    CRYPTO_ALGORITHM_FAMILY_KDF: _ClassVar[CryptoAlgorithmFamily]
    CRYPTO_ALGORITHM_FAMILY_KEY_WRAP: _ClassVar[CryptoAlgorithmFamily]
    CRYPTO_ALGORITHM_FAMILY_HPKE: _ClassVar[CryptoAlgorithmFamily]

class SignatureAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNATURE_ALGORITHM_UNSPECIFIED: _ClassVar[SignatureAlgorithm]
    SIGNATURE_ALGORITHM_ED25519: _ClassVar[SignatureAlgorithm]
    SIGNATURE_ALGORITHM_ECDSA_P256_SHA256: _ClassVar[SignatureAlgorithm]
    SIGNATURE_ALGORITHM_ECDSA_P384_SHA384: _ClassVar[SignatureAlgorithm]
    SIGNATURE_ALGORITHM_ECDSA_P521_SHA512: _ClassVar[SignatureAlgorithm]
    SIGNATURE_ALGORITHM_ECDSA_SECP256K1_SHA256: _ClassVar[SignatureAlgorithm]
    SIGNATURE_ALGORITHM_BIP340_SCHNORR_SECP256K1_SHA256: _ClassVar[SignatureAlgorithm]
    SIGNATURE_ALGORITHM_RSA_PKCS1V15_SHA1: _ClassVar[SignatureAlgorithm]
    SIGNATURE_ALGORITHM_RSA_PKCS1V15_SHA256: _ClassVar[SignatureAlgorithm]
    SIGNATURE_ALGORITHM_RSA_PKCS1V15_SHA384: _ClassVar[SignatureAlgorithm]
    SIGNATURE_ALGORITHM_RSA_PKCS1V15_SHA512: _ClassVar[SignatureAlgorithm]
    SIGNATURE_ALGORITHM_RSA_PSS_SHA1_MGF1_SHA1: _ClassVar[SignatureAlgorithm]
    SIGNATURE_ALGORITHM_RSA_PSS_SHA256_MGF1_SHA256: _ClassVar[SignatureAlgorithm]
    SIGNATURE_ALGORITHM_RSA_PSS_SHA384_MGF1_SHA384: _ClassVar[SignatureAlgorithm]
    SIGNATURE_ALGORITHM_RSA_PSS_SHA512_MGF1_SHA512: _ClassVar[SignatureAlgorithm]
    SIGNATURE_ALGORITHM_ML_DSA_44: _ClassVar[SignatureAlgorithm]
    SIGNATURE_ALGORITHM_ML_DSA_65: _ClassVar[SignatureAlgorithm]
    SIGNATURE_ALGORITHM_ML_DSA_87: _ClassVar[SignatureAlgorithm]
    SIGNATURE_ALGORITHM_SLH_DSA_SHA2_128S: _ClassVar[SignatureAlgorithm]

class KeyAgreementAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEY_AGREEMENT_ALGORITHM_UNSPECIFIED: _ClassVar[KeyAgreementAlgorithm]
    KEY_AGREEMENT_ALGORITHM_X25519: _ClassVar[KeyAgreementAlgorithm]
    KEY_AGREEMENT_ALGORITHM_P256_ECDH: _ClassVar[KeyAgreementAlgorithm]

class KemAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEM_ALGORITHM_UNSPECIFIED: _ClassVar[KemAlgorithm]
    KEM_ALGORITHM_ML_KEM_512: _ClassVar[KemAlgorithm]
    KEM_ALGORITHM_ML_KEM_768: _ClassVar[KemAlgorithm]
    KEM_ALGORITHM_ML_KEM_1024: _ClassVar[KemAlgorithm]
    KEM_ALGORITHM_X_WING_768: _ClassVar[KemAlgorithm]
    KEM_ALGORITHM_X_WING_1024: _ClassVar[KemAlgorithm]

class HpkeSuite(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HPKE_SUITE_UNSPECIFIED: _ClassVar[HpkeSuite]
    HPKE_SUITE_DHKEM_P256_HKDF_SHA256_HKDF_SHA256_AES_256_GCM: _ClassVar[HpkeSuite]
    HPKE_SUITE_DHKEM_X25519_HKDF_SHA256_HKDF_SHA256_CHACHA20_POLY1305: _ClassVar[HpkeSuite]

class AeadAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AEAD_ALGORITHM_UNSPECIFIED: _ClassVar[AeadAlgorithm]
    AEAD_ALGORITHM_AES_256_GCM: _ClassVar[AeadAlgorithm]
    AEAD_ALGORITHM_AES_256_GCM_SIV: _ClassVar[AeadAlgorithm]
    AEAD_ALGORITHM_CHACHA20_POLY1305: _ClassVar[AeadAlgorithm]
    AEAD_ALGORITHM_XCHACHA20_POLY1305: _ClassVar[AeadAlgorithm]

class HashAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HASH_ALGORITHM_UNSPECIFIED: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHA2_256: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHA2_384: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHA2_512: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHA3_224: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHA3_256: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHA3_384: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHA3_512: _ClassVar[HashAlgorithm]

class MacAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MAC_ALGORITHM_UNSPECIFIED: _ClassVar[MacAlgorithm]
    MAC_ALGORITHM_HMAC_SHA256: _ClassVar[MacAlgorithm]
    MAC_ALGORITHM_HMAC_SHA512: _ClassVar[MacAlgorithm]

class KdfAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KDF_ALGORITHM_UNSPECIFIED: _ClassVar[KdfAlgorithm]
    KDF_ALGORITHM_HKDF_SHA256: _ClassVar[KdfAlgorithm]
    KDF_ALGORITHM_ARGON2ID: _ClassVar[KdfAlgorithm]
    KDF_ALGORITHM_PBKDF2_HMAC_SHA256: _ClassVar[KdfAlgorithm]
    KDF_ALGORITHM_PBKDF2_HMAC_SHA512: _ClassVar[KdfAlgorithm]

class KeyWrapAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEY_WRAP_ALGORITHM_UNSPECIFIED: _ClassVar[KeyWrapAlgorithm]
    KEY_WRAP_ALGORITHM_AES_256_KW: _ClassVar[KeyWrapAlgorithm]

class MulticodecKeyAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MULTICODEC_KEY_ALGORITHM_UNSPECIFIED: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_ED25519_PUB: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_X25519_PUB: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_SECP256K1_PUB: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_P256_PUB: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_P384_PUB: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_P521_PUB: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_ED448_PUB: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_RSA_PUB: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_ML_KEM_512_PUB: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_ML_KEM_768_PUB: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_ML_KEM_1024_PUB: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_ML_DSA_44_PUB: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_ML_DSA_65_PUB: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_ML_DSA_87_PUB: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_ED25519_PRIV: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_X25519_PRIV: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_SECP256K1_PRIV: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_P256_PRIV: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_P384_PRIV: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_P521_PRIV: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_ED448_PRIV: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_RSA_PRIV: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_ML_KEM_512_PRIV: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_ML_KEM_768_PRIV: _ClassVar[MulticodecKeyAlgorithm]
    MULTICODEC_KEY_ALGORITHM_ML_KEM_1024_PRIV: _ClassVar[MulticodecKeyAlgorithm]
CRYPTO_ALGORITHM_FAMILY_UNSPECIFIED: CryptoAlgorithmFamily
CRYPTO_ALGORITHM_FAMILY_SIGNATURE: CryptoAlgorithmFamily
CRYPTO_ALGORITHM_FAMILY_KEY_AGREEMENT: CryptoAlgorithmFamily
CRYPTO_ALGORITHM_FAMILY_KEM: CryptoAlgorithmFamily
CRYPTO_ALGORITHM_FAMILY_AEAD: CryptoAlgorithmFamily
CRYPTO_ALGORITHM_FAMILY_HASH: CryptoAlgorithmFamily
CRYPTO_ALGORITHM_FAMILY_MAC: CryptoAlgorithmFamily
CRYPTO_ALGORITHM_FAMILY_KDF: CryptoAlgorithmFamily
CRYPTO_ALGORITHM_FAMILY_KEY_WRAP: CryptoAlgorithmFamily
CRYPTO_ALGORITHM_FAMILY_HPKE: CryptoAlgorithmFamily
SIGNATURE_ALGORITHM_UNSPECIFIED: SignatureAlgorithm
SIGNATURE_ALGORITHM_ED25519: SignatureAlgorithm
SIGNATURE_ALGORITHM_ECDSA_P256_SHA256: SignatureAlgorithm
SIGNATURE_ALGORITHM_ECDSA_P384_SHA384: SignatureAlgorithm
SIGNATURE_ALGORITHM_ECDSA_P521_SHA512: SignatureAlgorithm
SIGNATURE_ALGORITHM_ECDSA_SECP256K1_SHA256: SignatureAlgorithm
SIGNATURE_ALGORITHM_BIP340_SCHNORR_SECP256K1_SHA256: SignatureAlgorithm
SIGNATURE_ALGORITHM_RSA_PKCS1V15_SHA1: SignatureAlgorithm
SIGNATURE_ALGORITHM_RSA_PKCS1V15_SHA256: SignatureAlgorithm
SIGNATURE_ALGORITHM_RSA_PKCS1V15_SHA384: SignatureAlgorithm
SIGNATURE_ALGORITHM_RSA_PKCS1V15_SHA512: SignatureAlgorithm
SIGNATURE_ALGORITHM_RSA_PSS_SHA1_MGF1_SHA1: SignatureAlgorithm
SIGNATURE_ALGORITHM_RSA_PSS_SHA256_MGF1_SHA256: SignatureAlgorithm
SIGNATURE_ALGORITHM_RSA_PSS_SHA384_MGF1_SHA384: SignatureAlgorithm
SIGNATURE_ALGORITHM_RSA_PSS_SHA512_MGF1_SHA512: SignatureAlgorithm
SIGNATURE_ALGORITHM_ML_DSA_44: SignatureAlgorithm
SIGNATURE_ALGORITHM_ML_DSA_65: SignatureAlgorithm
SIGNATURE_ALGORITHM_ML_DSA_87: SignatureAlgorithm
SIGNATURE_ALGORITHM_SLH_DSA_SHA2_128S: SignatureAlgorithm
KEY_AGREEMENT_ALGORITHM_UNSPECIFIED: KeyAgreementAlgorithm
KEY_AGREEMENT_ALGORITHM_X25519: KeyAgreementAlgorithm
KEY_AGREEMENT_ALGORITHM_P256_ECDH: KeyAgreementAlgorithm
KEM_ALGORITHM_UNSPECIFIED: KemAlgorithm
KEM_ALGORITHM_ML_KEM_512: KemAlgorithm
KEM_ALGORITHM_ML_KEM_768: KemAlgorithm
KEM_ALGORITHM_ML_KEM_1024: KemAlgorithm
KEM_ALGORITHM_X_WING_768: KemAlgorithm
KEM_ALGORITHM_X_WING_1024: KemAlgorithm
HPKE_SUITE_UNSPECIFIED: HpkeSuite
HPKE_SUITE_DHKEM_P256_HKDF_SHA256_HKDF_SHA256_AES_256_GCM: HpkeSuite
HPKE_SUITE_DHKEM_X25519_HKDF_SHA256_HKDF_SHA256_CHACHA20_POLY1305: HpkeSuite
AEAD_ALGORITHM_UNSPECIFIED: AeadAlgorithm
AEAD_ALGORITHM_AES_256_GCM: AeadAlgorithm
AEAD_ALGORITHM_AES_256_GCM_SIV: AeadAlgorithm
AEAD_ALGORITHM_CHACHA20_POLY1305: AeadAlgorithm
AEAD_ALGORITHM_XCHACHA20_POLY1305: AeadAlgorithm
HASH_ALGORITHM_UNSPECIFIED: HashAlgorithm
HASH_ALGORITHM_SHA2_256: HashAlgorithm
HASH_ALGORITHM_SHA2_384: HashAlgorithm
HASH_ALGORITHM_SHA2_512: HashAlgorithm
HASH_ALGORITHM_SHA3_224: HashAlgorithm
HASH_ALGORITHM_SHA3_256: HashAlgorithm
HASH_ALGORITHM_SHA3_384: HashAlgorithm
HASH_ALGORITHM_SHA3_512: HashAlgorithm
MAC_ALGORITHM_UNSPECIFIED: MacAlgorithm
MAC_ALGORITHM_HMAC_SHA256: MacAlgorithm
MAC_ALGORITHM_HMAC_SHA512: MacAlgorithm
KDF_ALGORITHM_UNSPECIFIED: KdfAlgorithm
KDF_ALGORITHM_HKDF_SHA256: KdfAlgorithm
KDF_ALGORITHM_ARGON2ID: KdfAlgorithm
KDF_ALGORITHM_PBKDF2_HMAC_SHA256: KdfAlgorithm
KDF_ALGORITHM_PBKDF2_HMAC_SHA512: KdfAlgorithm
KEY_WRAP_ALGORITHM_UNSPECIFIED: KeyWrapAlgorithm
KEY_WRAP_ALGORITHM_AES_256_KW: KeyWrapAlgorithm
MULTICODEC_KEY_ALGORITHM_UNSPECIFIED: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_ED25519_PUB: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_X25519_PUB: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_SECP256K1_PUB: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_P256_PUB: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_P384_PUB: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_P521_PUB: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_ED448_PUB: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_RSA_PUB: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_ML_KEM_512_PUB: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_ML_KEM_768_PUB: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_ML_KEM_1024_PUB: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_ML_DSA_44_PUB: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_ML_DSA_65_PUB: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_ML_DSA_87_PUB: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_ED25519_PRIV: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_X25519_PRIV: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_SECP256K1_PRIV: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_P256_PRIV: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_P384_PRIV: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_P521_PRIV: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_ED448_PRIV: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_RSA_PRIV: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_ML_KEM_512_PRIV: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_ML_KEM_768_PRIV: MulticodecKeyAlgorithm
MULTICODEC_KEY_ALGORITHM_ML_KEM_1024_PRIV: MulticodecKeyAlgorithm

class CryptoAlgorithmIdentifier(_message.Message):
    __slots__ = ("signature", "key_agreement", "kem", "hpke", "aead", "hash", "mac", "kdf", "key_wrap", "multicodec_key")
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    KEY_AGREEMENT_FIELD_NUMBER: _ClassVar[int]
    KEM_FIELD_NUMBER: _ClassVar[int]
    HPKE_FIELD_NUMBER: _ClassVar[int]
    AEAD_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    KDF_FIELD_NUMBER: _ClassVar[int]
    KEY_WRAP_FIELD_NUMBER: _ClassVar[int]
    MULTICODEC_KEY_FIELD_NUMBER: _ClassVar[int]
    signature: SignatureAlgorithm
    key_agreement: KeyAgreementAlgorithm
    kem: KemAlgorithm
    hpke: HpkeSuite
    aead: AeadAlgorithm
    hash: HashAlgorithm
    mac: MacAlgorithm
    kdf: KdfAlgorithm
    key_wrap: KeyWrapAlgorithm
    multicodec_key: MulticodecKeyAlgorithm
    def __init__(self, signature: _Optional[_Union[SignatureAlgorithm, str]] = ..., key_agreement: _Optional[_Union[KeyAgreementAlgorithm, str]] = ..., kem: _Optional[_Union[KemAlgorithm, str]] = ..., hpke: _Optional[_Union[HpkeSuite, str]] = ..., aead: _Optional[_Union[AeadAlgorithm, str]] = ..., hash: _Optional[_Union[HashAlgorithm, str]] = ..., mac: _Optional[_Union[MacAlgorithm, str]] = ..., kdf: _Optional[_Union[KdfAlgorithm, str]] = ..., key_wrap: _Optional[_Union[KeyWrapAlgorithm, str]] = ..., multicodec_key: _Optional[_Union[MulticodecKeyAlgorithm, str]] = ...) -> None: ...

class JsonWebKey(_message.Message):
    __slots__ = ("algorithm", "public_key", "canonical_jcs")
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_JCS_FIELD_NUMBER: _ClassVar[int]
    algorithm: CryptoAlgorithmIdentifier
    public_key: bytes
    canonical_jcs: bytes
    def __init__(self, algorithm: _Optional[_Union[CryptoAlgorithmIdentifier, _Mapping]] = ..., public_key: _Optional[bytes] = ..., canonical_jcs: _Optional[bytes] = ...) -> None: ...

class JsonWebKeySet(_message.Message):
    __slots__ = ("keys",)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[JsonWebKey]
    def __init__(self, keys: _Optional[_Iterable[_Union[JsonWebKey, _Mapping]]] = ...) -> None: ...
