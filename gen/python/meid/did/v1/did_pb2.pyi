from google.protobuf import struct_pb2 as _struct_pb2
from reallyme.crypto.v1 import crypto_pb2 as _crypto_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CoreKey(_message.Message):
    __slots__ = ("id", "type", "algorithm", "public_key_multibase")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_MULTIBASE_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    algorithm: _crypto_pb2.CryptoAlgorithmIdentifier
    public_key_multibase: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., algorithm: _Optional[_Union[_crypto_pb2.CryptoAlgorithmIdentifier, _Mapping]] = ..., public_key_multibase: _Optional[str] = ...) -> None: ...

class VerificationMethod(_message.Message):
    __slots__ = ("id", "type", "controller", "public_key_multibase", "algorithm")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_MULTIBASE_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    controller: str
    public_key_multibase: str
    algorithm: _crypto_pb2.CryptoAlgorithmIdentifier
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., controller: _Optional[str] = ..., public_key_multibase: _Optional[str] = ..., algorithm: _Optional[_Union[_crypto_pb2.CryptoAlgorithmIdentifier, _Mapping]] = ...) -> None: ...

class Service(_message.Message):
    __slots__ = ("id", "type", "service_endpoint")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    service_endpoint: _struct_pb2.Value
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., service_endpoint: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...

class MessagingServiceEndpoint(_message.Message):
    __slots__ = ("uri", "pre_keys")
    URI_FIELD_NUMBER: _ClassVar[int]
    PRE_KEYS_FIELD_NUMBER: _ClassVar[int]
    uri: str
    pre_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, uri: _Optional[str] = ..., pre_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class Attestation(_message.Message):
    __slots__ = ("alg", "vm", "sig")
    ALG_FIELD_NUMBER: _ClassVar[int]
    VM_FIELD_NUMBER: _ClassVar[int]
    SIG_FIELD_NUMBER: _ClassVar[int]
    alg: _crypto_pb2.SignatureAlgorithm
    vm: str
    sig: bytes
    def __init__(self, alg: _Optional[_Union[_crypto_pb2.SignatureAlgorithm, str]] = ..., vm: _Optional[str] = ..., sig: _Optional[bytes] = ...) -> None: ...

class DataIntegrityProof(_message.Message):
    __slots__ = ("type", "cryptosuite", "verification_method", "created", "jws", "proof_purpose")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CRYPTOSUITE_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    JWS_FIELD_NUMBER: _ClassVar[int]
    PROOF_PURPOSE_FIELD_NUMBER: _ClassVar[int]
    type: str
    cryptosuite: str
    verification_method: str
    created: str
    jws: str
    proof_purpose: str
    def __init__(self, type: _Optional[str] = ..., cryptosuite: _Optional[str] = ..., verification_method: _Optional[str] = ..., created: _Optional[str] = ..., jws: _Optional[str] = ..., proof_purpose: _Optional[str] = ...) -> None: ...

class DomainVerification(_message.Message):
    __slots__ = ("type", "domain", "method", "dns", "well_known")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    DNS_FIELD_NUMBER: _ClassVar[int]
    WELL_KNOWN_FIELD_NUMBER: _ClassVar[int]
    type: str
    domain: str
    method: str
    dns: DNSBinding
    well_known: WellKnownBinding
    def __init__(self, type: _Optional[str] = ..., domain: _Optional[str] = ..., method: _Optional[str] = ..., dns: _Optional[_Union[DNSBinding, _Mapping]] = ..., well_known: _Optional[_Union[WellKnownBinding, _Mapping]] = ...) -> None: ...

class DNSBinding(_message.Message):
    __slots__ = ("record_name", "txt_value")
    RECORD_NAME_FIELD_NUMBER: _ClassVar[int]
    TXT_VALUE_FIELD_NUMBER: _ClassVar[int]
    record_name: str
    txt_value: str
    def __init__(self, record_name: _Optional[str] = ..., txt_value: _Optional[str] = ...) -> None: ...

class WellKnownBinding(_message.Message):
    __slots__ = ("uri", "content")
    URI_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    uri: str
    content: str
    def __init__(self, uri: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class UpdatePolicy(_message.Message):
    __slots__ = ("allowed_verification_methods", "threshold")
    ALLOWED_VERIFICATION_METHODS_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    allowed_verification_methods: _containers.RepeatedScalarFieldContainer[str]
    threshold: int
    def __init__(self, allowed_verification_methods: _Optional[_Iterable[str]] = ..., threshold: _Optional[int] = ...) -> None: ...

class Core(_message.Message):
    __slots__ = ("id", "sequence", "prev", "nonce", "controller", "controller_keys", "authentication_keys", "assertion_keys", "key_agreement_keys", "services", "update_policy")
    ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    PREV_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_KEYS_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_KEYS_FIELD_NUMBER: _ClassVar[int]
    ASSERTION_KEYS_FIELD_NUMBER: _ClassVar[int]
    KEY_AGREEMENT_KEYS_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    UPDATE_POLICY_FIELD_NUMBER: _ClassVar[int]
    id: str
    sequence: int
    prev: str
    nonce: bytes
    controller: _struct_pb2.Value
    controller_keys: _containers.RepeatedCompositeFieldContainer[CoreKey]
    authentication_keys: _containers.RepeatedScalarFieldContainer[str]
    assertion_keys: _containers.RepeatedScalarFieldContainer[str]
    key_agreement_keys: _containers.RepeatedScalarFieldContainer[str]
    services: _containers.RepeatedCompositeFieldContainer[Service]
    update_policy: UpdatePolicy
    def __init__(self, id: _Optional[str] = ..., sequence: _Optional[int] = ..., prev: _Optional[str] = ..., nonce: _Optional[bytes] = ..., controller: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., controller_keys: _Optional[_Iterable[_Union[CoreKey, _Mapping]]] = ..., authentication_keys: _Optional[_Iterable[str]] = ..., assertion_keys: _Optional[_Iterable[str]] = ..., key_agreement_keys: _Optional[_Iterable[str]] = ..., services: _Optional[_Iterable[_Union[Service, _Mapping]]] = ..., update_policy: _Optional[_Union[UpdatePolicy, _Mapping]] = ...) -> None: ...

class GenesisBinding(_message.Message):
    __slots__ = ("nonce", "update_policy", "controller_keys")
    NONCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_POLICY_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_KEYS_FIELD_NUMBER: _ClassVar[int]
    nonce: bytes
    update_policy: UpdatePolicy
    controller_keys: _containers.RepeatedCompositeFieldContainer[CoreKey]
    def __init__(self, nonce: _Optional[bytes] = ..., update_policy: _Optional[_Union[UpdatePolicy, _Mapping]] = ..., controller_keys: _Optional[_Iterable[_Union[CoreKey, _Mapping]]] = ...) -> None: ...

class DIDDocument(_message.Message):
    __slots__ = ("id", "controller", "context", "also_known_as", "biometric_protected", "hardware_bound", "device_model", "user_verification_method", "sequence", "prev", "current_core", "core_cbor", "key_history", "verification_method", "authentication", "assertion_method", "capability_invocation", "key_agreement", "service", "update_policy", "attestations", "proof", "domain_verification", "nonce", "eudi_level_of_assurance", "eudi_schema_version")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ALSO_KNOWN_AS_FIELD_NUMBER: _ClassVar[int]
    BIOMETRIC_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_BOUND_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MODEL_FIELD_NUMBER: _ClassVar[int]
    USER_VERIFICATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    PREV_FIELD_NUMBER: _ClassVar[int]
    CURRENT_CORE_FIELD_NUMBER: _ClassVar[int]
    CORE_CBOR_FIELD_NUMBER: _ClassVar[int]
    KEY_HISTORY_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    ASSERTION_METHOD_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_INVOCATION_FIELD_NUMBER: _ClassVar[int]
    KEY_AGREEMENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_POLICY_FIELD_NUMBER: _ClassVar[int]
    ATTESTATIONS_FIELD_NUMBER: _ClassVar[int]
    PROOF_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    EUDI_LEVEL_OF_ASSURANCE_FIELD_NUMBER: _ClassVar[int]
    EUDI_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    id: str
    controller: _struct_pb2.Value
    context: _containers.RepeatedScalarFieldContainer[str]
    also_known_as: _containers.RepeatedScalarFieldContainer[str]
    biometric_protected: bool
    hardware_bound: bool
    device_model: str
    user_verification_method: str
    sequence: int
    prev: str
    current_core: str
    core_cbor: bytes
    key_history: _containers.RepeatedScalarFieldContainer[str]
    verification_method: _containers.RepeatedCompositeFieldContainer[VerificationMethod]
    authentication: _containers.RepeatedScalarFieldContainer[str]
    assertion_method: _containers.RepeatedScalarFieldContainer[str]
    capability_invocation: _containers.RepeatedScalarFieldContainer[str]
    key_agreement: _containers.RepeatedScalarFieldContainer[str]
    service: _containers.RepeatedCompositeFieldContainer[Service]
    update_policy: UpdatePolicy
    attestations: _containers.RepeatedCompositeFieldContainer[Attestation]
    proof: DataIntegrityProof
    domain_verification: _containers.RepeatedCompositeFieldContainer[DomainVerification]
    nonce: bytes
    eudi_level_of_assurance: str
    eudi_schema_version: str
    def __init__(self, id: _Optional[str] = ..., controller: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., context: _Optional[_Iterable[str]] = ..., also_known_as: _Optional[_Iterable[str]] = ..., biometric_protected: _Optional[bool] = ..., hardware_bound: _Optional[bool] = ..., device_model: _Optional[str] = ..., user_verification_method: _Optional[str] = ..., sequence: _Optional[int] = ..., prev: _Optional[str] = ..., current_core: _Optional[str] = ..., core_cbor: _Optional[bytes] = ..., key_history: _Optional[_Iterable[str]] = ..., verification_method: _Optional[_Iterable[_Union[VerificationMethod, _Mapping]]] = ..., authentication: _Optional[_Iterable[str]] = ..., assertion_method: _Optional[_Iterable[str]] = ..., capability_invocation: _Optional[_Iterable[str]] = ..., key_agreement: _Optional[_Iterable[str]] = ..., service: _Optional[_Iterable[_Union[Service, _Mapping]]] = ..., update_policy: _Optional[_Union[UpdatePolicy, _Mapping]] = ..., attestations: _Optional[_Iterable[_Union[Attestation, _Mapping]]] = ..., proof: _Optional[_Union[DataIntegrityProof, _Mapping]] = ..., domain_verification: _Optional[_Iterable[_Union[DomainVerification, _Mapping]]] = ..., nonce: _Optional[bytes] = ..., eudi_level_of_assurance: _Optional[str] = ..., eudi_schema_version: _Optional[str] = ...) -> None: ...
