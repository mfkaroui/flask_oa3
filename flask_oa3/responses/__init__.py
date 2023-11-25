from .response import BaseResponse

class ContinueResponse(BaseResponse):
    """
    indicates that the initial part of a request has been received and has not yet been rejected by the server.

    SpecTitle:
        RFC7231#6.2.1
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.2.1
    """
    __STATUS_CODE__: int = 100
    __PHRASE__: str = "Continue"

class SwitchingProtocolsResponse(BaseResponse):
    """
    indicates that the server understands and is willing to comply with the client's request, via the Upgrade header field, for a change in the application protocol being used on this connection.

    SpecTitle:
        RFC7231#6.2.2
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.2.2
    """
    __STATUS_CODE__: int = 101
    __PHRASE__: str = "Switching Protocols"

class OKResponse(BaseResponse):
    """
    indicates that the request has succeeded.

    SpecTitle:
        RFC7231#6.3.1
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.3.1
    """
    __STATUS_CODE__: int = 200
    __PHRASE__: str = "OK"

class CreatedResponse(BaseResponse):
    """
    indicates that the request has been fulfilled and has resulted in one or more new resources being created.

    SpecTitle:
        RFC7231#6.3.2
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.3.2
    """
    __STATUS_CODE__: int = 201
    __PHRASE__: str = "Created"

class AcceptedResponse(BaseResponse):
    """
    indicates that the request has been accepted for processing, but the processing has not been completed.

    SpecTitle:
        RFC7231#6.3.3
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.3.3
    """
    __STATUS_CODE__: int = 202
    __PHRASE__: str = "Accepted"

class NonAuthoritativeInformationResponse(BaseResponse):
    """
    indicates that the request was successful but the enclosed payload has been modified from that of the origin server's 200 (OK) response by a transforming proxy.

    SpecTitle:
        RFC7231#6.3.4
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.3.4
    """
    __STATUS_CODE__: int = 203
    __PHRASE__: str = "Non-Authoritative Information"

class NoContentResponse(BaseResponse):
    """
    indicates that the server has successfully fulfilled the request and that there is no additional content to send in the response payload body.

    SpecTitle:
        RFC7231#6.3.5
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.3.5
    """
    __STATUS_CODE__: int = 204
    __PHRASE__: str = "No Content"

class ResetContentResponse(BaseResponse):
    """
    indicates that the server has fulfilled the request and desires that the user agent reset the document view, which caused the request to be sent, to its original state as received from the origin server.

    SpecTitle:
        RFC7231#6.3.6
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.3.6
    """
    __STATUS_CODE__: int = 205
    __PHRASE__: str = "Reset Content"

class PartialContentResponse(BaseResponse):
    """
    indicates that the server is successfully fulfilling a range request for the target resource by transferring one or more parts of the selected representation that correspond to the satisfiable ranges found in the requests's Range header field.

    SpecTitle:
        RFC7233#4.1
    
    SpecReference:
        https://tools.ietf.org/html/rfc7233#section-4.1
    """
    __STATUS_CODE__: int = 206
    __PHRASE__: str = "Partial Content"

class MultipleChoicesResponse(BaseResponse):
    """
    indicates that the target resource has more than one representation, each with its own more specific identifier, and information about the alternatives is being provided so that the user (or user agent) can select a preferred representation by redirecting its request to one or more of those identifiers.

    SpecTitle:
        RFC7231#6.4.1
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.4.1
    """
    __STATUS_CODE__: int = 300
    __PHRASE__: str = "Multiple Choices"

class MovedPermanentlyResponse(BaseResponse):
    """
    indicates that the target resource has been assigned a new permanent URI and any future references to this resource ought to use one of the enclosed URIs.

    SpecTitle:
        RFC7231#6.4.2
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.4.2
    """
    __STATUS_CODE__: int = 301
    __PHRASE__: str = "Moved Permanently"

class FoundResponse(BaseResponse):
    """
    indicates that the target resource resides temporarily under a different URI.

    SpecTitle:
        RFC7231#6.4.3
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.4.3
    """
    __STATUS_CODE__: int = 302
    __PHRASE__: str = "Found"

class SeeOtherResponse(BaseResponse):
    """
    indicates that the server is redirecting the user agent to a different resource, as indicated by a URI in the Location header field, that is intended to provide an indirect response to the original request.

    SpecTitle:
        RFC7231#6.4.4
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.4.4
    """
    __STATUS_CODE__: int = 303
    __PHRASE__: str = "See Other"

class NotModifiedResponse(BaseResponse):
    """
    indicates that a conditional GET request has been received and would have resulted in a 200 (OK) response if it were not for the fact that the condition has evaluated to false.

    SpecTitle:
        RFC7232#4.1
    
    SpecReference:
        https://tools.ietf.org/html/rfc7232#section-4.1
    """
    __STATUS_CODE__: int = 304
    __PHRASE__: str = "Not Modified"

class UseProxyResponse(BaseResponse):
    """
    *deprecated*

    SpecTitle:
        RFC7231#6.4.5
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.4.5
    """
    __STATUS_CODE__: int = 305
    __PHRASE__: str = "Use Proxy"

class TemporaryRedirectResponse(BaseResponse):
    """
    indicates that the target resource resides temporarily under a different URI and the user agent MUST NOT change the request method if it performs an automatic redirection to that URI.

    SpecTitle:
        RFC7231#6.4.7
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.4.7
    """
    __STATUS_CODE__: int = 307
    __PHRASE__: str = "Temporary Redirect"

class BadRequestResponse(BaseResponse):
    """
    indicates that the server cannot or will not process the request because the received syntax is invalid, nonsensical, or exceeds some limitation on what the server is willing to process.

    SpecTitle:
        RFC7231#6.5.1
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.1
    """
    __STATUS_CODE__: int = 400
    __PHRASE__: str = "Bad Request"

class UnauthorizedResponse(BaseResponse):
    """
    indicates that the request has not been applied because it lacks valid authentication credentials for the target resource.

    SpecTitle:
        RFC7235#6.3.1
    
    SpecReference:
        https://tools.ietf.org/html/rfc7235#section-3.1
    """
    __STATUS_CODE__: int = 401
    __PHRASE__: str = "Unauthorized"

class PaymentRequiredResponse(BaseResponse):
    """
    *reserved*

    SpecTitle:
        RFC7231#6.5.2
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.2
    """
    __STATUS_CODE__: int = 402
    __PHRASE__: str = "Payment Required"

class ForbiddenResponse(BaseResponse):
    """
    indicates that the server understood the request but refuses to authorize it.

    SpecTitle:
        RFC7231#6.5.3
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.3
    """
    __STATUS_CODE__: int = 403
    __PHRASE__: str = "Forbidden"

class NotFoundResponse(BaseResponse):
    """
    indicates that the origin server did not find a current representation for the target resource or is not willing to disclose that one exists.

    SpecTitle:
        RFC7231#6.5.4
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.4
    """
    __STATUS_CODE__: int = 404
    __PHRASE__: str = "Not Found"

class MethodNotAllowedResponse(BaseResponse):
    """
    indicates that the method specified in the request-line is known by the origin server but not supported by the target resource.

    SpecTitle:
        RFC7231#6.5.5
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.5
    """
    __STATUS_CODE__: int = 405
    __PHRASE__: str = "Method Not Allowed"

class NotAcceptableResponse(BaseResponse):
    """
    indicates that the target resource does not have a current representation that would be acceptable to the user agent, according to the proactive negotiation header fields received in the request, and the server is unwilling to supply a default representation.

    SpecTitle:
        RFC7231#6.5.6
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.6
    """
    __STATUS_CODE__: int = 406
    __PHRASE__: str = "Not Acceptable"

class ProxyAuthenticationRequiredResponse(BaseResponse):
    """
    is similar to 401 (Unauthorized), but indicates that the client needs to authenticate itself in order to use a proxy.

    SpecTitle:
        RFC7235#3.2
    
    SpecReference:
        https://tools.ietf.org/html/rfc7235#section-3.2
    """
    __STATUS_CODE__: int = 407
    __PHRASE__: str = "Proxy Authentication Required"

class RequestTimeoutResponse(BaseResponse):
    """
    indicates that the server did not receive a complete request message within the time that it was prepared to wait.

    SpecTitle:
        RFC7231#6.5.7
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.7
    """
    __STATUS_CODE__: int = 408
    __PHRASE__: str = "Request Timeout"

class ConflictResponse(BaseResponse):
    """
    indicates that the request could not be completed due to a conflict with the current state of the resource.

    SpecTitle:
        RFC7231#6.5.8
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.8
    """
    __STATUS_CODE__: int = 409
    __PHRASE__: str = "Conflict"

class GoneResponse(BaseResponse):
    """
    indicates that access to the target resource is no longer available at the origin server and that this condition is likely to be permanent.

    SpecTitle:
        RFC7231#6.5.9
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.9
    """
    __STATUS_CODE__: int = 410
    __PHRASE__: str = "Gone"

class LengthRequiredResponse(BaseResponse):
    """
    indicates that the server refuses to accept the request without a defined Content-Length.

    SpecTitle:
        RFC7231#6.5.10
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.10
    """
    __STATUS_CODE__: int = 411
    __PHRASE__: str = "Length Required"

class PreconditionFailedResponse(BaseResponse):
    """
    indicates that one or more preconditions given in the request header fields evaluated to false when tested on the server.

    SpecTitle:
        RFC7232#4.2
    
    SpecReference:
        https://tools.ietf.org/html/rfc7232#section-4.2
    """
    __STATUS_CODE__: int = 412
    __PHRASE__: str = "Precondition Failed"

class PayloadTooLargeResponse(BaseResponse):
    """
    indicates that the server is refusing to process a request because the request payload is larger than the server is willing or able to process.

    SpecTitle:
        RFC7231#6.5.11
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.11
    """
    __STATUS_CODE__: int = 413
    __PHRASE__: str = "Payload Too Large"

class URITooLongResponse(BaseResponse):
    """
    indicates that the server is refusing to service the request because the request-target is longer than the server is willing to interpret.

    SpecTitle:
        RFC7231#6.5.12
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.12
    """
    __STATUS_CODE__: int = 414
    __PHRASE__: str = "URI Too Long"

class UnsupportedMediaTypeResponse(BaseResponse):
    """
    indicates that the origin server is refusing to service the request because the payload is in a format not supported by the target resource for this method.

    SpecTitle:
        RFC7231#6.5.13
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.13
    """
    __STATUS_CODE__: int = 415
    __PHRASE__: str = "Unsupported Media Type"

class RangeNotSatisfiableResponse(BaseResponse):
    """
    indicates that none of the ranges in the request's Range header field overlap the current extent of the selected resource or that the set of ranges requested has been rejected due to invalid ranges or an excessive request of small or overlapping ranges.

    SpecTitle:
        RFC7233#4.4
    
    SpecReference:
        https://tools.ietf.org/html/rfc7233#section-4.4
    """
    __STATUS_CODE__: int = 416
    __PHRASE__: str = "Range Not Satisfiable"

class ExpectationFailedResponse(BaseResponse):
    """
    indicates that the expectation given in the request's Expect header field could not be met by at least one of the inbound servers.

    SpecTitle:
        RFC7231#6.5.14
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.14
    """
    __STATUS_CODE__: int = 417
    __PHRASE__: str = "Expectation Failed"

class UpgradeRequiredResponse(BaseResponse):
    """
    indicates that the server refuses to perform the request using the current protocol but might be willing to do so after the client upgrades to a different protocol.

    SpecTitle:
        RFC7231#6.5.15
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.15
    """
    __STATUS_CODE__: int = 426
    __PHRASE__: str = "Upgrade Required"

class InternalServerErrorResponse(BaseResponse):
    """
    indicates that the server encountered an unexpected condition that prevented it from fulfilling the request.

    SpecTitle:
        RFC7231#6.6.1
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.6.1
    """
    __STATUS_CODE__: int = 500
    __PHRASE__: str = "Internal Server Error"

class NotImplementedResponse(BaseResponse):
    """
    indicates that the server does not support the functionality required to fulfill the request.

    SpecTitle:
        RFC7231#6.6.2
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.6.2
    """
    __STATUS_CODE__: int = 501
    __PHRASE__: str = "Not Implemented"

class BadGatewayResponse(BaseResponse):
    """
    indicates that the server, while acting as a gateway or proxy, received an invalid response from an inbound server it accessed while attempting to fulfill the request.

    SpecTitle:
        RFC7231#6.6.3
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.6.3
    """
    __STATUS_CODE__: int = 502
    __PHRASE__: str = "Bad Gateway"

class ServiceUnavailableResponse(BaseResponse):
    """
    indicates that the server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay.

    SpecTitle:
        RFC7231#6.6.4
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.6.4
    """
    __STATUS_CODE__: int = 503
    __PHRASE__: str = "Service Unavailable"

class GatewayTimeoutResponse(BaseResponse):
    """
    indicates that the server, while acting as a gateway or proxy, did not receive a timely response from an upstream server it needed to access in order to complete the request.

    SpecTitle:
        RFC7231#6.6.5
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.6.5
    """
    __STATUS_CODE__: int = 504
    __PHRASE__: str = "Gateway Time-out"

class HTTPVersionNotSupportedResponse(BaseResponse):
    """
    indicates that the server does not support, or refuses to support, the protocol version that was used in the request message.

    SpecTitle:
        RFC7231#6.6.6
    
    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.6.6
    """
    __STATUS_CODE__: int = 505
    __PHRASE__: str = "HTTP Version Not Supported"

class ProcessingResponse(BaseResponse):
    """
    is an interim response used to inform the client that the server has accepted the complete request, but has not yet completed it.

    SpecTitle:
        RFC5218#10.1
    
    SpecReference:
        https://tools.ietf.org/html/rfc2518#section-10.1
    """
    __STATUS_CODE__: int = 102
    __PHRASE__: str = "Processing"

class MultiStatusResponse(BaseResponse):
    """
    provides status for multiple independent operations.

    SpecTitle:
        RFC5218#10.2
    
    SpecReference:
        https://tools.ietf.org/html/rfc2518#section-10.2
    """
    __STATUS_CODE__: int = 207
    __PHRASE__: str = "Multi-Status"

class IMUsedResponse(BaseResponse):
    """
    The server has fulfilled a GET request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance.

    SpecTitle:
        RFC3229#10.4.1
    
    SpecReference:
        https://tools.ietf.org/html/rfc3229#section-10.4.1
    """
    __STATUS_CODE__: int = 226
    __PHRASE__: str = "IM Used"

class PermanentRedirectResponse(BaseResponse):
    """
    The target resource has been assigned a new permanent URI and any future references to this resource outght to use one of the enclosed URIs. [...] This status code is similar to 301 Moved Permanently (Section 7.3.2 of rfc7231), except that it does not allow rewriting the request method from POST to GET.

    SpecTitle:
        RFC7538
    
    SpecReference:
        https://tools.ietf.org/html/rfc7538
    """
    __STATUS_CODE__: int = 308
    __PHRASE__: str = "Permanent Redirect"

class UnprocessableEntityResponse(BaseResponse):
    """
    means the server understands the content type of the request entity (hence a 415(Unsupported Media Type) status code is inappropriate), and the syntax of the request entity is correct (thus a 400 (Bad Request) status code is inappropriate) but was unable to process the contained instructions.

    SpecTitle:
        RFC5218#10.3
    
    SpecReference:
        https://tools.ietf.org/html/rfc2518#section-10.3
    """
    __STATUS_CODE__: int = 422
    __PHRASE__: str = "Unprocessable Entity"

class LockedResponse(BaseResponse):
    """
    means the source or destination resource of a method is locked.

    SpecTitle:
        RFC5218#10.4
    
    SpecReference:
        https://tools.ietf.org/html/rfc2518#section-10.4
    """
    __STATUS_CODE__: int = 423
    __PHRASE__: str = "Locked"

class FailedDependencyResponse(BaseResponse):
    """
    means that the method could not be performed on the resource because the requested action depended on another action and that action failed.

    SpecTitle:
        RFC5218#10.5
    
    SpecReference:
        https://tools.ietf.org/html/rfc2518#section-10.5
    """
    __STATUS_CODE__: int = 424
    __PHRASE__: str = "Failed Dependency"

class PreconditionRequiredResponse(BaseResponse):
    """
    indicates that the origin server requires the request to be conditional.

    SpecTitle:
        RFC6585#3
    
    SpecReference:
        https://tools.ietf.org/html/rfc6585#section-3
    """
    __STATUS_CODE__: int = 428
    __PHRASE__: str = "Precondition Required"

class TooManyRequestsResponse(BaseResponse):
    """
    indicates that the user has sent too many requests in a given amount of time (rate limiting).

    SpecTitle:
        RFC6585#4
    
    SpecReference:
        https://tools.ietf.org/html/rfc6585#section-4
    """
    __STATUS_CODE__: int = 429
    __PHRASE__: str = "Too Many Requests"

class RequestHeaderFieldsTooLargeResponse(BaseResponse):
    """
    indicates that the server is unwilling to process the request because its header fields are too large.

    SpecTitle:
        RFC6585#5
    
    SpecReference:
        https://tools.ietf.org/html/rfc6585#section-5
    """
    __STATUS_CODE__: int = 431
    __PHRASE__: str = "Request Header Fields Too Large"

class UnavailableForLegalReasonsResponse(BaseResponse):
    """
    This status code indicates that the server is denying access to the resource in response to a legal demand.

    SpecTitle:
        draft-ietf-httpbis-legally-restricted-status
    
    SpecReference:
        https://tools.ietf.org/html/draft-ietf-httpbis-legally-restricted-status
    """
    __STATUS_CODE__: int = 451
    __PHRASE__: str = "Unavailable For Legal Reasons"

class VariantAlsoNegotiatesResponse(BaseResponse):
    """
    indicates that the server has an internal configuration error: the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper end point in the negotiation process.

    SpecTitle:
        RFC2295#8.1
    
    SpecReference:
        https://tools.ietf.org/html/rfc2295#section-8.1
    """
    __STATUS_CODE__: int = 506
    __PHRASE__: str = "Variant Also Negotiates"

class InsufficientStorageResponse(BaseResponse):
    """
    means the method could not be performed on the resource because the server is unable to store the representation needed to successfully complete the request.

    SpecTitle:
        RFC5218#10.6
    
    SpecReference:
        https://tools.ietf.org/html/rfc2518#section-10.6
    """
    __STATUS_CODE__: int = 507
    __PHRASE__: str = "Insufficient Storage"

class NetworkAuthenticationRequiredResponse(BaseResponse):
    """
    indicates that the client needs to authenticate to gain network access.

    SpecTitle:
        RFC6585#6
    
    SpecReference:
        https://tools.ietf.org/html/rfc6585#section-6
    """
    __STATUS_CODE__: int = 511
    __PHRASE__: str = "Network Authentication Required"

