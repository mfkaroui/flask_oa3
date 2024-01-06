### AUTO-GENERATED ###
from typing import Union, Type
from .response import Response, ResponseType


class ResponseContinue(Response):
    """
    indicates that the initial part of a request has been received and has not yet been rejected by the server.

    StatusCode:
        100

    SpecTitle:
        RFC7231#6.2.1

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.2.1
    """

    __STATUS_CODE__: int = 100
    __PHRASE__: str = "Continue"

    @property
    def component_name(self) -> str:
        return "ResponseContinue"


class ResponseSwitchingProtocols(Response):
    """
    indicates that the server understands and is willing to comply with the client's request, via the Upgrade header field, for a change in the application protocol being used on this connection.

    StatusCode:
        101

    SpecTitle:
        RFC7231#6.2.2

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.2.2
    """

    __STATUS_CODE__: int = 101
    __PHRASE__: str = "Switching Protocols"

    @property
    def component_name(self) -> str:
        return "ResponseSwitchingProtocols"


class ResponseOk(Response):
    """
    indicates that the request has succeeded.

    StatusCode:
        200

    SpecTitle:
        RFC7231#6.3.1

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.3.1
    """

    __STATUS_CODE__: int = 200
    __PHRASE__: str = "OK"

    @property
    def component_name(self) -> str:
        return "ResponseOk"


class ResponseCreated(Response):
    """
    indicates that the request has been fulfilled and has resulted in one or more new resources being created.

    StatusCode:
        201

    SpecTitle:
        RFC7231#6.3.2

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.3.2
    """

    __STATUS_CODE__: int = 201
    __PHRASE__: str = "Created"

    @property
    def component_name(self) -> str:
        return "ResponseCreated"


class ResponseAccepted(Response):
    """
    indicates that the request has been accepted for processing, but the processing has not been completed.

    StatusCode:
        202

    SpecTitle:
        RFC7231#6.3.3

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.3.3
    """

    __STATUS_CODE__: int = 202
    __PHRASE__: str = "Accepted"

    @property
    def component_name(self) -> str:
        return "ResponseAccepted"


class ResponseNonAuthoritativeInformation(Response):
    """
    indicates that the request was successful but the enclosed payload has been modified from that of the origin server's 200 (OK) response by a transforming proxy.

    StatusCode:
        203

    SpecTitle:
        RFC7231#6.3.4

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.3.4
    """

    __STATUS_CODE__: int = 203
    __PHRASE__: str = "Non-Authoritative Information"

    @property
    def component_name(self) -> str:
        return "ResponseNonAuthoritativeInformation"


class ResponseNoContent(Response):
    """
    indicates that the server has successfully fulfilled the request and that there is no additional content to send in the response payload body.

    StatusCode:
        204

    SpecTitle:
        RFC7231#6.3.5

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.3.5
    """

    __STATUS_CODE__: int = 204
    __PHRASE__: str = "No Content"

    @property
    def component_name(self) -> str:
        return "ResponseNoContent"


class ResponseResetContent(Response):
    """
    indicates that the server has fulfilled the request and desires that the user agent reset the document view, which caused the request to be sent, to its original state as received from the origin server.

    StatusCode:
        205

    SpecTitle:
        RFC7231#6.3.6

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.3.6
    """

    __STATUS_CODE__: int = 205
    __PHRASE__: str = "Reset Content"

    @property
    def component_name(self) -> str:
        return "ResponseResetContent"


class ResponsePartialContent(Response):
    """
    indicates that the server is successfully fulfilling a range request for the target resource by transferring one or more parts of the selected representation that correspond to the satisfiable ranges found in the requests's Range header field.

    StatusCode:
        206

    SpecTitle:
        RFC7233#4.1

    SpecReference:
        https://tools.ietf.org/html/rfc7233#section-4.1
    """

    __STATUS_CODE__: int = 206
    __PHRASE__: str = "Partial Content"

    @property
    def component_name(self) -> str:
        return "ResponsePartialContent"


class ResponseMultipleChoices(Response):
    """
    indicates that the target resource has more than one representation, each with its own more specific identifier, and information about the alternatives is being provided so that the user (or user agent) can select a preferred representation by redirecting its request to one or more of those identifiers.

    StatusCode:
        300

    SpecTitle:
        RFC7231#6.4.1

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.4.1
    """

    __STATUS_CODE__: int = 300
    __PHRASE__: str = "Multiple Choices"

    @property
    def component_name(self) -> str:
        return "ResponseMultipleChoices"


class ResponseMovedPermanently(Response):
    """
    indicates that the target resource has been assigned a new permanent URI and any future references to this resource ought to use one of the enclosed URIs.

    StatusCode:
        301

    SpecTitle:
        RFC7231#6.4.2

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.4.2
    """

    __STATUS_CODE__: int = 301
    __PHRASE__: str = "Moved Permanently"

    @property
    def component_name(self) -> str:
        return "ResponseMovedPermanently"


class ResponseFound(Response):
    """
    indicates that the target resource resides temporarily under a different URI.

    StatusCode:
        302

    SpecTitle:
        RFC7231#6.4.3

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.4.3
    """

    __STATUS_CODE__: int = 302
    __PHRASE__: str = "Found"

    @property
    def component_name(self) -> str:
        return "ResponseFound"


class ResponseSeeOther(Response):
    """
    indicates that the server is redirecting the user agent to a different resource, as indicated by a URI in the Location header field, that is intended to provide an indirect response to the original request.

    StatusCode:
        303

    SpecTitle:
        RFC7231#6.4.4

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.4.4
    """

    __STATUS_CODE__: int = 303
    __PHRASE__: str = "See Other"

    @property
    def component_name(self) -> str:
        return "ResponseSeeOther"


class ResponseNotModified(Response):
    """
    indicates that a conditional GET request has been received and would have resulted in a 200 (OK) response if it were not for the fact that the condition has evaluated to false.

    StatusCode:
        304

    SpecTitle:
        RFC7232#4.1

    SpecReference:
        https://tools.ietf.org/html/rfc7232#section-4.1
    """

    __STATUS_CODE__: int = 304
    __PHRASE__: str = "Not Modified"

    @property
    def component_name(self) -> str:
        return "ResponseNotModified"


class ResponseUseProxy(Response):
    """
    *deprecated*

    StatusCode:
        305

    SpecTitle:
        RFC7231#6.4.5

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.4.5
    """

    __STATUS_CODE__: int = 305
    __PHRASE__: str = "Use Proxy"

    @property
    def component_name(self) -> str:
        return "ResponseUseProxy"


class ResponseTemporaryRedirect(Response):
    """
    indicates that the target resource resides temporarily under a different URI and the user agent MUST NOT change the request method if it performs an automatic redirection to that URI.

    StatusCode:
        307

    SpecTitle:
        RFC7231#6.4.7

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.4.7
    """

    __STATUS_CODE__: int = 307
    __PHRASE__: str = "Temporary Redirect"

    @property
    def component_name(self) -> str:
        return "ResponseTemporaryRedirect"


class ResponseBadRequest(Response):
    """
    indicates that the server cannot or will not process the request because the received syntax is invalid, nonsensical, or exceeds some limitation on what the server is willing to process.

    StatusCode:
        400

    SpecTitle:
        RFC7231#6.5.1

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.1
    """

    __STATUS_CODE__: int = 400
    __PHRASE__: str = "Bad Request"

    @property
    def component_name(self) -> str:
        return "ResponseBadRequest"


class ResponseUnauthorized(Response):
    """
    indicates that the request has not been applied because it lacks valid authentication credentials for the target resource.

    StatusCode:
        401

    SpecTitle:
        RFC7235#6.3.1

    SpecReference:
        https://tools.ietf.org/html/rfc7235#section-3.1
    """

    __STATUS_CODE__: int = 401
    __PHRASE__: str = "Unauthorized"

    @property
    def component_name(self) -> str:
        return "ResponseUnauthorized"


class ResponsePaymentRequired(Response):
    """
    *reserved*

    StatusCode:
        402

    SpecTitle:
        RFC7231#6.5.2

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.2
    """

    __STATUS_CODE__: int = 402
    __PHRASE__: str = "Payment Required"

    @property
    def component_name(self) -> str:
        return "ResponsePaymentRequired"


class ResponseForbidden(Response):
    """
    indicates that the server understood the request but refuses to authorize it.

    StatusCode:
        403

    SpecTitle:
        RFC7231#6.5.3

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.3
    """

    __STATUS_CODE__: int = 403
    __PHRASE__: str = "Forbidden"

    @property
    def component_name(self) -> str:
        return "ResponseForbidden"


class ResponseNotFound(Response):
    """
    indicates that the origin server did not find a current representation for the target resource or is not willing to disclose that one exists.

    StatusCode:
        404

    SpecTitle:
        RFC7231#6.5.4

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.4
    """

    __STATUS_CODE__: int = 404
    __PHRASE__: str = "Not Found"

    @property
    def component_name(self) -> str:
        return "ResponseNotFound"


class ResponseMethodNotAllowed(Response):
    """
    indicates that the method specified in the request-line is known by the origin server but not supported by the target resource.

    StatusCode:
        405

    SpecTitle:
        RFC7231#6.5.5

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.5
    """

    __STATUS_CODE__: int = 405
    __PHRASE__: str = "Method Not Allowed"

    @property
    def component_name(self) -> str:
        return "ResponseMethodNotAllowed"


class ResponseNotAcceptable(Response):
    """
    indicates that the target resource does not have a current representation that would be acceptable to the user agent, according to the proactive negotiation header fields received in the request, and the server is unwilling to supply a default representation.

    StatusCode:
        406

    SpecTitle:
        RFC7231#6.5.6

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.6
    """

    __STATUS_CODE__: int = 406
    __PHRASE__: str = "Not Acceptable"

    @property
    def component_name(self) -> str:
        return "ResponseNotAcceptable"


class ResponseProxyAuthenticationRequired(Response):
    """
    is similar to 401 (Unauthorized), but indicates that the client needs to authenticate itself in order to use a proxy.

    StatusCode:
        407

    SpecTitle:
        RFC7235#3.2

    SpecReference:
        https://tools.ietf.org/html/rfc7235#section-3.2
    """

    __STATUS_CODE__: int = 407
    __PHRASE__: str = "Proxy Authentication Required"

    @property
    def component_name(self) -> str:
        return "ResponseProxyAuthenticationRequired"


class ResponseRequestTimeout(Response):
    """
    indicates that the server did not receive a complete request message within the time that it was prepared to wait.

    StatusCode:
        408

    SpecTitle:
        RFC7231#6.5.7

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.7
    """

    __STATUS_CODE__: int = 408
    __PHRASE__: str = "Request Timeout"

    @property
    def component_name(self) -> str:
        return "ResponseRequestTimeout"


class ResponseConflict(Response):
    """
    indicates that the request could not be completed due to a conflict with the current state of the resource.

    StatusCode:
        409

    SpecTitle:
        RFC7231#6.5.8

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.8
    """

    __STATUS_CODE__: int = 409
    __PHRASE__: str = "Conflict"

    @property
    def component_name(self) -> str:
        return "ResponseConflict"


class ResponseGone(Response):
    """
    indicates that access to the target resource is no longer available at the origin server and that this condition is likely to be permanent.

    StatusCode:
        410

    SpecTitle:
        RFC7231#6.5.9

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.9
    """

    __STATUS_CODE__: int = 410
    __PHRASE__: str = "Gone"

    @property
    def component_name(self) -> str:
        return "ResponseGone"


class ResponseLengthRequired(Response):
    """
    indicates that the server refuses to accept the request without a defined Content-Length.

    StatusCode:
        411

    SpecTitle:
        RFC7231#6.5.10

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.10
    """

    __STATUS_CODE__: int = 411
    __PHRASE__: str = "Length Required"

    @property
    def component_name(self) -> str:
        return "ResponseLengthRequired"


class ResponsePreconditionFailed(Response):
    """
    indicates that one or more preconditions given in the request header fields evaluated to false when tested on the server.

    StatusCode:
        412

    SpecTitle:
        RFC7232#4.2

    SpecReference:
        https://tools.ietf.org/html/rfc7232#section-4.2
    """

    __STATUS_CODE__: int = 412
    __PHRASE__: str = "Precondition Failed"

    @property
    def component_name(self) -> str:
        return "ResponsePreconditionFailed"


class ResponsePayloadTooLarge(Response):
    """
    indicates that the server is refusing to process a request because the request payload is larger than the server is willing or able to process.

    StatusCode:
        413

    SpecTitle:
        RFC7231#6.5.11

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.11
    """

    __STATUS_CODE__: int = 413
    __PHRASE__: str = "Payload Too Large"

    @property
    def component_name(self) -> str:
        return "ResponsePayloadTooLarge"


class ResponseUriTooLong(Response):
    """
    indicates that the server is refusing to service the request because the request-target is longer than the server is willing to interpret.

    StatusCode:
        414

    SpecTitle:
        RFC7231#6.5.12

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.12
    """

    __STATUS_CODE__: int = 414
    __PHRASE__: str = "URI Too Long"

    @property
    def component_name(self) -> str:
        return "ResponseUriTooLong"


class ResponseUnsupportedMediaType(Response):
    """
    indicates that the origin server is refusing to service the request because the payload is in a format not supported by the target resource for this method.

    StatusCode:
        415

    SpecTitle:
        RFC7231#6.5.13

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.13
    """

    __STATUS_CODE__: int = 415
    __PHRASE__: str = "Unsupported Media Type"

    @property
    def component_name(self) -> str:
        return "ResponseUnsupportedMediaType"


class ResponseRangeNotSatisfiable(Response):
    """
    indicates that none of the ranges in the request's Range header field overlap the current extent of the selected resource or that the set of ranges requested has been rejected due to invalid ranges or an excessive request of small or overlapping ranges.

    StatusCode:
        416

    SpecTitle:
        RFC7233#4.4

    SpecReference:
        https://tools.ietf.org/html/rfc7233#section-4.4
    """

    __STATUS_CODE__: int = 416
    __PHRASE__: str = "Range Not Satisfiable"

    @property
    def component_name(self) -> str:
        return "ResponseRangeNotSatisfiable"


class ResponseExpectationFailed(Response):
    """
    indicates that the expectation given in the request's Expect header field could not be met by at least one of the inbound servers.

    StatusCode:
        417

    SpecTitle:
        RFC7231#6.5.14

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.14
    """

    __STATUS_CODE__: int = 417
    __PHRASE__: str = "Expectation Failed"

    @property
    def component_name(self) -> str:
        return "ResponseExpectationFailed"


class ResponseUpgradeRequired(Response):
    """
    indicates that the server refuses to perform the request using the current protocol but might be willing to do so after the client upgrades to a different protocol.

    StatusCode:
        426

    SpecTitle:
        RFC7231#6.5.15

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.5.15
    """

    __STATUS_CODE__: int = 426
    __PHRASE__: str = "Upgrade Required"

    @property
    def component_name(self) -> str:
        return "ResponseUpgradeRequired"


class ResponseInternalServerError(Response):
    """
    indicates that the server encountered an unexpected condition that prevented it from fulfilling the request.

    StatusCode:
        500

    SpecTitle:
        RFC7231#6.6.1

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.6.1
    """

    __STATUS_CODE__: int = 500
    __PHRASE__: str = "Internal Server Error"

    @property
    def component_name(self) -> str:
        return "ResponseInternalServerError"


class ResponseNotImplemented(Response):
    """
    indicates that the server does not support the functionality required to fulfill the request.

    StatusCode:
        501

    SpecTitle:
        RFC7231#6.6.2

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.6.2
    """

    __STATUS_CODE__: int = 501
    __PHRASE__: str = "Not Implemented"

    @property
    def component_name(self) -> str:
        return "ResponseNotImplemented"


class ResponseBadGateway(Response):
    """
    indicates that the server, while acting as a gateway or proxy, received an invalid response from an inbound server it accessed while attempting to fulfill the request.

    StatusCode:
        502

    SpecTitle:
        RFC7231#6.6.3

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.6.3
    """

    __STATUS_CODE__: int = 502
    __PHRASE__: str = "Bad Gateway"

    @property
    def component_name(self) -> str:
        return "ResponseBadGateway"


class ResponseServiceUnavailable(Response):
    """
    indicates that the server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay.

    StatusCode:
        503

    SpecTitle:
        RFC7231#6.6.4

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.6.4
    """

    __STATUS_CODE__: int = 503
    __PHRASE__: str = "Service Unavailable"

    @property
    def component_name(self) -> str:
        return "ResponseServiceUnavailable"


class ResponseGatewayTimeOut(Response):
    """
    indicates that the server, while acting as a gateway or proxy, did not receive a timely response from an upstream server it needed to access in order to complete the request.

    StatusCode:
        504

    SpecTitle:
        RFC7231#6.6.5

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.6.5
    """

    __STATUS_CODE__: int = 504
    __PHRASE__: str = "Gateway Time-out"

    @property
    def component_name(self) -> str:
        return "ResponseGatewayTimeOut"


class ResponseHttpVersionNotSupported(Response):
    """
    indicates that the server does not support, or refuses to support, the protocol version that was used in the request message.

    StatusCode:
        505

    SpecTitle:
        RFC7231#6.6.6

    SpecReference:
        https://tools.ietf.org/html/rfc7231#section-6.6.6
    """

    __STATUS_CODE__: int = 505
    __PHRASE__: str = "HTTP Version Not Supported"

    @property
    def component_name(self) -> str:
        return "ResponseHttpVersionNotSupported"


class ResponseProcessing(Response):
    """
    is an interim response used to inform the client that the server has accepted the complete request, but has not yet completed it.

    StatusCode:
        102

    SpecTitle:
        RFC5218#10.1

    SpecReference:
        https://tools.ietf.org/html/rfc2518#section-10.1
    """

    __STATUS_CODE__: int = 102
    __PHRASE__: str = "Processing"

    @property
    def component_name(self) -> str:
        return "ResponseProcessing"


class ResponseMultiStatus(Response):
    """
    provides status for multiple independent operations.

    StatusCode:
        207

    SpecTitle:
        RFC5218#10.2

    SpecReference:
        https://tools.ietf.org/html/rfc2518#section-10.2
    """

    __STATUS_CODE__: int = 207
    __PHRASE__: str = "Multi-Status"

    @property
    def component_name(self) -> str:
        return "ResponseMultiStatus"


class ResponseImUsed(Response):
    """
    The server has fulfilled a GET request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance.

    StatusCode:
        226

    SpecTitle:
        RFC3229#10.4.1

    SpecReference:
        https://tools.ietf.org/html/rfc3229#section-10.4.1
    """

    __STATUS_CODE__: int = 226
    __PHRASE__: str = "IM Used"

    @property
    def component_name(self) -> str:
        return "ResponseImUsed"


class ResponsePermanentRedirect(Response):
    """
    The target resource has been assigned a new permanent URI and any future references to this resource outght to use one of the enclosed URIs. [...] This status code is similar to 301 Moved Permanently (Section 7.3.2 of rfc7231), except that it does not allow rewriting the request method from POST to GET.

    StatusCode:
        308

    SpecTitle:
        RFC7538

    SpecReference:
        https://tools.ietf.org/html/rfc7538
    """

    __STATUS_CODE__: int = 308
    __PHRASE__: str = "Permanent Redirect"

    @property
    def component_name(self) -> str:
        return "ResponsePermanentRedirect"


class ResponseUnprocessableEntity(Response):
    """
    means the server understands the content type of the request entity (hence a 415(Unsupported Media Type) status code is inappropriate), and the syntax of the request entity is correct (thus a 400 (Bad Request) status code is inappropriate) but was unable to process the contained instructions.

    StatusCode:
        422

    SpecTitle:
        RFC5218#10.3

    SpecReference:
        https://tools.ietf.org/html/rfc2518#section-10.3
    """

    __STATUS_CODE__: int = 422
    __PHRASE__: str = "Unprocessable Entity"

    @property
    def component_name(self) -> str:
        return "ResponseUnprocessableEntity"


class ResponseLocked(Response):
    """
    means the source or destination resource of a method is locked.

    StatusCode:
        423

    SpecTitle:
        RFC5218#10.4

    SpecReference:
        https://tools.ietf.org/html/rfc2518#section-10.4
    """

    __STATUS_CODE__: int = 423
    __PHRASE__: str = "Locked"

    @property
    def component_name(self) -> str:
        return "ResponseLocked"


class ResponseFailedDependency(Response):
    """
    means that the method could not be performed on the resource because the requested action depended on another action and that action failed.

    StatusCode:
        424

    SpecTitle:
        RFC5218#10.5

    SpecReference:
        https://tools.ietf.org/html/rfc2518#section-10.5
    """

    __STATUS_CODE__: int = 424
    __PHRASE__: str = "Failed Dependency"

    @property
    def component_name(self) -> str:
        return "ResponseFailedDependency"


class ResponsePreconditionRequired(Response):
    """
    indicates that the origin server requires the request to be conditional.

    StatusCode:
        428

    SpecTitle:
        RFC6585#3

    SpecReference:
        https://tools.ietf.org/html/rfc6585#section-3
    """

    __STATUS_CODE__: int = 428
    __PHRASE__: str = "Precondition Required"

    @property
    def component_name(self) -> str:
        return "ResponsePreconditionRequired"


class ResponseTooManyRequests(Response):
    """
    indicates that the user has sent too many requests in a given amount of time (rate limiting).

    StatusCode:
        429

    SpecTitle:
        RFC6585#4

    SpecReference:
        https://tools.ietf.org/html/rfc6585#section-4
    """

    __STATUS_CODE__: int = 429
    __PHRASE__: str = "Too Many Requests"

    @property
    def component_name(self) -> str:
        return "ResponseTooManyRequests"


class ResponseRequestHeaderFieldsTooLarge(Response):
    """
    indicates that the server is unwilling to process the request because its header fields are too large.

    StatusCode:
        431

    SpecTitle:
        RFC6585#5

    SpecReference:
        https://tools.ietf.org/html/rfc6585#section-5
    """

    __STATUS_CODE__: int = 431
    __PHRASE__: str = "Request Header Fields Too Large"

    @property
    def component_name(self) -> str:
        return "ResponseRequestHeaderFieldsTooLarge"


class ResponseUnavailableForLegalReasons(Response):
    """
    This status code indicates that the server is denying access to the resource in response to a legal demand.

    StatusCode:
        451

    SpecTitle:
        draft-ietf-httpbis-legally-restricted-status

    SpecReference:
        https://tools.ietf.org/html/draft-ietf-httpbis-legally-restricted-status
    """

    __STATUS_CODE__: int = 451
    __PHRASE__: str = "Unavailable For Legal Reasons"

    @property
    def component_name(self) -> str:
        return "ResponseUnavailableForLegalReasons"


class ResponseVariantAlsoNegotiates(Response):
    """
    indicates that the server has an internal configuration error: the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper end point in the negotiation process.

    StatusCode:
        506

    SpecTitle:
        RFC2295#8.1

    SpecReference:
        https://tools.ietf.org/html/rfc2295#section-8.1
    """

    __STATUS_CODE__: int = 506
    __PHRASE__: str = "Variant Also Negotiates"

    @property
    def component_name(self) -> str:
        return "ResponseVariantAlsoNegotiates"


class ResponseInsufficientStorage(Response):
    """
    means the method could not be performed on the resource because the server is unable to store the representation needed to successfully complete the request.

    StatusCode:
        507

    SpecTitle:
        RFC5218#10.6

    SpecReference:
        https://tools.ietf.org/html/rfc2518#section-10.6
    """

    __STATUS_CODE__: int = 507
    __PHRASE__: str = "Insufficient Storage"

    @property
    def component_name(self) -> str:
        return "ResponseInsufficientStorage"


class ResponseNetworkAuthenticationRequired(Response):
    """
    indicates that the client needs to authenticate to gain network access.

    StatusCode:
        511

    SpecTitle:
        RFC6585#6

    SpecReference:
        https://tools.ietf.org/html/rfc6585#section-6
    """

    __STATUS_CODE__: int = 511
    __PHRASE__: str = "Network Authentication Required"

    @property
    def component_name(self) -> str:
        return "ResponseNetworkAuthenticationRequired"


def get_response_by_status_code(status_code: int) -> Union[Type[Response], None]:
    """
    Retrieves a Response object corresponding to a given HTTP status code.

    This function maps standard HTTP status codes to their respective Response class objects. It provides a convenient way to access Response objects based on the status code encountered in HTTP communication.

    Args:
        status_code (int): The HTTP status code for which the corresponding Response object is required.

    Returns:
        Union[Type[Response], None]: Returns the Response class associated with the given status code. If the status code is not recognized, it returns None.
    """

    responses = {
        "100": ResponseContinue,
        "101": ResponseSwitchingProtocols,
        "200": ResponseOk,
        "201": ResponseCreated,
        "202": ResponseAccepted,
        "203": ResponseNonAuthoritativeInformation,
        "204": ResponseNoContent,
        "205": ResponseResetContent,
        "206": ResponsePartialContent,
        "300": ResponseMultipleChoices,
        "301": ResponseMovedPermanently,
        "302": ResponseFound,
        "303": ResponseSeeOther,
        "304": ResponseNotModified,
        "305": ResponseUseProxy,
        "307": ResponseTemporaryRedirect,
        "400": ResponseBadRequest,
        "401": ResponseUnauthorized,
        "402": ResponsePaymentRequired,
        "403": ResponseForbidden,
        "404": ResponseNotFound,
        "405": ResponseMethodNotAllowed,
        "406": ResponseNotAcceptable,
        "407": ResponseProxyAuthenticationRequired,
        "408": ResponseRequestTimeout,
        "409": ResponseConflict,
        "410": ResponseGone,
        "411": ResponseLengthRequired,
        "412": ResponsePreconditionFailed,
        "413": ResponsePayloadTooLarge,
        "414": ResponseUriTooLong,
        "415": ResponseUnsupportedMediaType,
        "416": ResponseRangeNotSatisfiable,
        "417": ResponseExpectationFailed,
        "426": ResponseUpgradeRequired,
        "500": ResponseInternalServerError,
        "501": ResponseNotImplemented,
        "502": ResponseBadGateway,
        "503": ResponseServiceUnavailable,
        "504": ResponseGatewayTimeOut,
        "505": ResponseHttpVersionNotSupported,
        "102": ResponseProcessing,
        "207": ResponseMultiStatus,
        "226": ResponseImUsed,
        "308": ResponsePermanentRedirect,
        "422": ResponseUnprocessableEntity,
        "423": ResponseLocked,
        "424": ResponseFailedDependency,
        "428": ResponsePreconditionRequired,
        "429": ResponseTooManyRequests,
        "431": ResponseRequestHeaderFieldsTooLarge,
        "451": ResponseUnavailableForLegalReasons,
        "506": ResponseVariantAlsoNegotiates,
        "507": ResponseInsufficientStorage,
        "511": ResponseNetworkAuthenticationRequired,
    }
    return responses.get(str(status_code), None)
