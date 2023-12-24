### AUTO-GENERATED ###
from pydantic import BaseModel, Field, computed_field, AnyUrl
from typing import ClassVar, Optional, List, Tuple, Dict, Union
from typing_extensions import Annotated
from .license import License

class PredefinedLicense(BaseModel):
    VERSION: ClassVar[str] = "2502b90"
    RELEASE_DATE: ClassVar[str] = "2023-11-10"

    url: Annotated[Optional[AnyUrl], Field(default=None, description="A URL to the license used for the API. This MUST be in the form of a URL. The url field is mutually exclusive of the identifier field.")]

    @computed_field(alias="name", description="REQUIRED. The license name used for the API.")
    @property
    def _name(self) -> str:
        return self.longName
    
    @computed_field(alias="identifier", description="An SPDX license expression for the API. The identifier field is mutually exclusive of the url field.")
    @property
    def _identifier(self) -> str:
        return self.licenseId

    @computed_field(alias="x-reference", description="x-reference.")
    @property
    def _reference(self) -> str:
        return str(self.reference)

    @computed_field(alias="x-reference-number", description="x-reference-number.")
    @property
    def _referenceNumber(self) -> str:
        return str(self.referenceNumber)

    @computed_field(alias="x-is-deprecated", description="x-is-deprecated.")
    @property
    def _isDeprecatedLicenseId(self) -> str:
        return str(self.isDeprecatedLicenseId)

    @computed_field(alias="x-is-osi-approved", description="x-is-osi-approved.")
    @property
    def _isOsiApproved(self) -> str:
        return str(self.isOsiApproved)

class License0BSD(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/0BSD.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/0BSD.json"
    referenceNumber: ClassVar[int] = 398
    longName: ClassVar[str] = "BSD Zero Clause License"
    licenseId: ClassVar[str] = "0BSD"
    seeAlso: ClassVar[List[str]] = ['http://landley.net/toybox/license.html', 'https://opensource.org/licenses/0BSD']
    isOsiApproved: ClassVar[bool] = True

class LicenseAal(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/AAL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/AAL.json"
    referenceNumber: ClassVar[int] = 402
    longName: ClassVar[str] = "Attribution Assurance License"
    licenseId: ClassVar[str] = "AAL"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/attribution']
    isOsiApproved: ClassVar[bool] = True

class LicenseAbstyles(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Abstyles.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Abstyles.json"
    referenceNumber: ClassVar[int] = 455
    longName: ClassVar[str] = "Abstyles License"
    licenseId: ClassVar[str] = "Abstyles"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Abstyles']
    isOsiApproved: ClassVar[bool] = False

class LicenseAdacoreDoc(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/AdaCore-doc.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/AdaCore-doc.json"
    referenceNumber: ClassVar[int] = 193
    longName: ClassVar[str] = "AdaCore Doc License"
    licenseId: ClassVar[str] = "AdaCore-doc"
    seeAlso: ClassVar[List[str]] = ['https://github.com/AdaCore/xmlada/blob/master/docs/index.rst', 'https://github.com/AdaCore/gnatcoll-core/blob/master/docs/index.rst', 'https://github.com/AdaCore/gnatcoll-db/blob/master/docs/index.rst']
    isOsiApproved: ClassVar[bool] = False

class LicenseAdobe2006(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Adobe-2006.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Adobe-2006.json"
    referenceNumber: ClassVar[int] = 125
    longName: ClassVar[str] = "Adobe Systems Incorporated Source Code License Agreement"
    licenseId: ClassVar[str] = "Adobe-2006"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/AdobeLicense']
    isOsiApproved: ClassVar[bool] = False

class LicenseAdobeDisplayPostscript(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Adobe-Display-PostScript.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Adobe-Display-PostScript.json"
    referenceNumber: ClassVar[int] = 595
    longName: ClassVar[str] = "Adobe Display PostScript License"
    licenseId: ClassVar[str] = "Adobe-Display-PostScript"
    seeAlso: ClassVar[List[str]] = ['https://gitlab.freedesktop.org/xorg/xserver/-/blob/master/COPYING?ref_type=heads#L752']
    isOsiApproved: ClassVar[bool] = False

class LicenseAdobeGlyph(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Adobe-Glyph.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Adobe-Glyph.json"
    referenceNumber: ClassVar[int] = 114
    longName: ClassVar[str] = "Adobe Glyph List License"
    licenseId: ClassVar[str] = "Adobe-Glyph"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/MIT#AdobeGlyph']
    isOsiApproved: ClassVar[bool] = False

class LicenseAdobeUtopia(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Adobe-Utopia.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Adobe-Utopia.json"
    referenceNumber: ClassVar[int] = 49
    longName: ClassVar[str] = "Adobe Utopia Font License"
    licenseId: ClassVar[str] = "Adobe-Utopia"
    seeAlso: ClassVar[List[str]] = ['https://gitlab.freedesktop.org/xorg/font/adobe-utopia-100dpi/-/blob/master/COPYING?ref_type=heads']
    isOsiApproved: ClassVar[bool] = False

class LicenseAdsl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/ADSL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/ADSL.json"
    referenceNumber: ClassVar[int] = 211
    longName: ClassVar[str] = "Amazon Digital Services License"
    licenseId: ClassVar[str] = "ADSL"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/AmazonDigitalServicesLicense']
    isOsiApproved: ClassVar[bool] = False

class LicenseAfl1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/AFL-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/AFL-1.1.json"
    referenceNumber: ClassVar[int] = 45
    longName: ClassVar[str] = "Academic Free License v1.1"
    licenseId: ClassVar[str] = "AFL-1.1"
    seeAlso: ClassVar[List[str]] = ['http://opensource.linux-mirror.org/licenses/afl-1.1.txt', 'http://wayback.archive.org/web/20021004124254/http://www.opensource.org/licenses/academic.php']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseAfl1_2(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/AFL-1.2.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/AFL-1.2.json"
    referenceNumber: ClassVar[int] = 297
    longName: ClassVar[str] = "Academic Free License v1.2"
    licenseId: ClassVar[str] = "AFL-1.2"
    seeAlso: ClassVar[List[str]] = ['http://opensource.linux-mirror.org/licenses/afl-1.2.txt', 'http://wayback.archive.org/web/20021204204652/http://www.opensource.org/licenses/academic.php']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseAfl2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/AFL-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/AFL-2.0.json"
    referenceNumber: ClassVar[int] = 147
    longName: ClassVar[str] = "Academic Free License v2.0"
    licenseId: ClassVar[str] = "AFL-2.0"
    seeAlso: ClassVar[List[str]] = ['http://wayback.archive.org/web/20060924134533/http://www.opensource.org/licenses/afl-2.0.txt']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseAfl2_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/AFL-2.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/AFL-2.1.json"
    referenceNumber: ClassVar[int] = 223
    longName: ClassVar[str] = "Academic Free License v2.1"
    licenseId: ClassVar[str] = "AFL-2.1"
    seeAlso: ClassVar[List[str]] = ['http://opensource.linux-mirror.org/licenses/afl-2.1.txt']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseAfl3_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/AFL-3.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/AFL-3.0.json"
    referenceNumber: ClassVar[int] = 166
    longName: ClassVar[str] = "Academic Free License v3.0"
    licenseId: ClassVar[str] = "AFL-3.0"
    seeAlso: ClassVar[List[str]] = ['http://www.rosenlaw.com/AFL3.0.htm', 'https://opensource.org/licenses/afl-3.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseAfmparse(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Afmparse.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Afmparse.json"
    referenceNumber: ClassVar[int] = 342
    longName: ClassVar[str] = "Afmparse License"
    licenseId: ClassVar[str] = "Afmparse"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Afmparse']
    isOsiApproved: ClassVar[bool] = False

class LicenseAgpl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/AGPL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/AGPL-1.0.json"
    referenceNumber: ClassVar[int] = 391
    longName: ClassVar[str] = "Affero General Public License v1.0"
    licenseId: ClassVar[str] = "AGPL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://www.affero.org/oagpl.html']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseAgpl1_0Only(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/AGPL-1.0-only.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/AGPL-1.0-only.json"
    referenceNumber: ClassVar[int] = 392
    longName: ClassVar[str] = "Affero General Public License v1.0 only"
    licenseId: ClassVar[str] = "AGPL-1.0-only"
    seeAlso: ClassVar[List[str]] = ['http://www.affero.org/oagpl.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseAgpl1_0OrLater(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/AGPL-1.0-or-later.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/AGPL-1.0-or-later.json"
    referenceNumber: ClassVar[int] = 17
    longName: ClassVar[str] = "Affero General Public License v1.0 or later"
    licenseId: ClassVar[str] = "AGPL-1.0-or-later"
    seeAlso: ClassVar[List[str]] = ['http://www.affero.org/oagpl.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseAgpl3_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/AGPL-3.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/AGPL-3.0.json"
    referenceNumber: ClassVar[int] = 337
    longName: ClassVar[str] = "GNU Affero General Public License v3.0"
    licenseId: ClassVar[str] = "AGPL-3.0"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/agpl.txt', 'https://opensource.org/licenses/AGPL-3.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseAgpl3_0Only(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/AGPL-3.0-only.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/AGPL-3.0-only.json"
    referenceNumber: ClassVar[int] = 139
    longName: ClassVar[str] = "GNU Affero General Public License v3.0 only"
    licenseId: ClassVar[str] = "AGPL-3.0-only"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/agpl.txt', 'https://opensource.org/licenses/AGPL-3.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseAgpl3_0OrLater(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/AGPL-3.0-or-later.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/AGPL-3.0-or-later.json"
    referenceNumber: ClassVar[int] = 140
    longName: ClassVar[str] = "GNU Affero General Public License v3.0 or later"
    licenseId: ClassVar[str] = "AGPL-3.0-or-later"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/agpl.txt', 'https://opensource.org/licenses/AGPL-3.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseAladdin(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Aladdin.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Aladdin.json"
    referenceNumber: ClassVar[int] = 382
    longName: ClassVar[str] = "Aladdin Free Public License"
    licenseId: ClassVar[str] = "Aladdin"
    seeAlso: ClassVar[List[str]] = ['http://pages.cs.wisc.edu/~ghost/doc/AFPL/6.01/Public.htm']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = False

class LicenseAmdplpa(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/AMDPLPA.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/AMDPLPA.json"
    referenceNumber: ClassVar[int] = 354
    longName: ClassVar[str] = "AMD's plpa_map.c License"
    licenseId: ClassVar[str] = "AMDPLPA"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/AMD_plpa_map_License']
    isOsiApproved: ClassVar[bool] = False

class LicenseAml(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/AML.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/AML.json"
    referenceNumber: ClassVar[int] = 212
    longName: ClassVar[str] = "Apple MIT License"
    licenseId: ClassVar[str] = "AML"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Apple_MIT_License']
    isOsiApproved: ClassVar[bool] = False

class LicenseAmlGlslang(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/AML-glslang.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/AML-glslang.json"
    referenceNumber: ClassVar[int] = 475
    longName: ClassVar[str] = "AML glslang variant License"
    licenseId: ClassVar[str] = "AML-glslang"
    seeAlso: ClassVar[List[str]] = ['https://github.com/KhronosGroup/glslang/blob/main/LICENSE.txt#L949', 'https://docs.omniverse.nvidia.com/install-guide/latest/common/licenses.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseAmpas(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/AMPAS.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/AMPAS.json"
    referenceNumber: ClassVar[int] = 565
    longName: ClassVar[str] = "Academy of Motion Picture Arts and Sciences BSD"
    licenseId: ClassVar[str] = "AMPAS"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/BSD#AMPASBSD']
    isOsiApproved: ClassVar[bool] = False

class LicenseAntlrPd(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/ANTLR-PD.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/ANTLR-PD.json"
    referenceNumber: ClassVar[int] = 136
    longName: ClassVar[str] = "ANTLR Software Rights Notice"
    licenseId: ClassVar[str] = "ANTLR-PD"
    seeAlso: ClassVar[List[str]] = ['http://www.antlr2.org/license.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseAntlrPdFallback(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/ANTLR-PD-fallback.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/ANTLR-PD-fallback.json"
    referenceNumber: ClassVar[int] = 15
    longName: ClassVar[str] = "ANTLR Software Rights Notice with license fallback"
    licenseId: ClassVar[str] = "ANTLR-PD-fallback"
    seeAlso: ClassVar[List[str]] = ['http://www.antlr2.org/license.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseApache1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Apache-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Apache-1.0.json"
    referenceNumber: ClassVar[int] = 43
    longName: ClassVar[str] = "Apache License 1.0"
    licenseId: ClassVar[str] = "Apache-1.0"
    seeAlso: ClassVar[List[str]] = ['http://www.apache.org/licenses/LICENSE-1.0']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseApache1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Apache-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Apache-1.1.json"
    referenceNumber: ClassVar[int] = 423
    longName: ClassVar[str] = "Apache License 1.1"
    licenseId: ClassVar[str] = "Apache-1.1"
    seeAlso: ClassVar[List[str]] = ['http://apache.org/licenses/LICENSE-1.1', 'https://opensource.org/licenses/Apache-1.1']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseApache2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Apache-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Apache-2.0.json"
    referenceNumber: ClassVar[int] = 180
    longName: ClassVar[str] = "Apache License 2.0"
    licenseId: ClassVar[str] = "Apache-2.0"
    seeAlso: ClassVar[List[str]] = ['https://www.apache.org/licenses/LICENSE-2.0', 'https://opensource.org/licenses/Apache-2.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseApafml(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/APAFML.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/APAFML.json"
    referenceNumber: ClassVar[int] = 289
    longName: ClassVar[str] = "Adobe Postscript AFM License"
    licenseId: ClassVar[str] = "APAFML"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/AdobePostscriptAFM']
    isOsiApproved: ClassVar[bool] = False

class LicenseApl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/APL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/APL-1.0.json"
    referenceNumber: ClassVar[int] = 304
    longName: ClassVar[str] = "Adaptive Public License 1.0"
    licenseId: ClassVar[str] = "APL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/APL-1.0']
    isOsiApproved: ClassVar[bool] = True

class LicenseAppS2p(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/App-s2p.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/App-s2p.json"
    referenceNumber: ClassVar[int] = 142
    longName: ClassVar[str] = "App::s2p License"
    licenseId: ClassVar[str] = "App-s2p"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/App-s2p']
    isOsiApproved: ClassVar[bool] = False

class LicenseApsl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/APSL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/APSL-1.0.json"
    referenceNumber: ClassVar[int] = 28
    longName: ClassVar[str] = "Apple Public Source License 1.0"
    licenseId: ClassVar[str] = "APSL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Apple_Public_Source_License_1.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = False

class LicenseApsl1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/APSL-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/APSL-1.1.json"
    referenceNumber: ClassVar[int] = 562
    longName: ClassVar[str] = "Apple Public Source License 1.1"
    licenseId: ClassVar[str] = "APSL-1.1"
    seeAlso: ClassVar[List[str]] = ['http://www.opensource.apple.com/source/IOSerialFamily/IOSerialFamily-7/APPLE_LICENSE']
    isOsiApproved: ClassVar[bool] = True

class LicenseApsl1_2(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/APSL-1.2.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/APSL-1.2.json"
    referenceNumber: ClassVar[int] = 556
    longName: ClassVar[str] = "Apple Public Source License 1.2"
    licenseId: ClassVar[str] = "APSL-1.2"
    seeAlso: ClassVar[List[str]] = ['http://www.samurajdata.se/opensource/mirror/licenses/apsl.php']
    isOsiApproved: ClassVar[bool] = True

class LicenseApsl2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/APSL-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/APSL-2.0.json"
    referenceNumber: ClassVar[int] = 472
    longName: ClassVar[str] = "Apple Public Source License 2.0"
    licenseId: ClassVar[str] = "APSL-2.0"
    seeAlso: ClassVar[List[str]] = ['http://www.opensource.apple.com/license/apsl/']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseArphic1999(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Arphic-1999.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Arphic-1999.json"
    referenceNumber: ClassVar[int] = 363
    longName: ClassVar[str] = "Arphic Public License"
    licenseId: ClassVar[str] = "Arphic-1999"
    seeAlso: ClassVar[List[str]] = ['http://ftp.gnu.org/gnu/non-gnu/chinese-fonts-truetype/LICENSE']
    isOsiApproved: ClassVar[bool] = False

class LicenseArtistic1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Artistic-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Artistic-1.0.json"
    referenceNumber: ClassVar[int] = 502
    longName: ClassVar[str] = "Artistic License 1.0"
    licenseId: ClassVar[str] = "Artistic-1.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/Artistic-1.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = False

class LicenseArtistic1_0Cl8(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Artistic-1.0-cl8.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Artistic-1.0-cl8.json"
    referenceNumber: ClassVar[int] = 336
    longName: ClassVar[str] = "Artistic License 1.0 w/clause 8"
    licenseId: ClassVar[str] = "Artistic-1.0-cl8"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/Artistic-1.0']
    isOsiApproved: ClassVar[bool] = True

class LicenseArtistic1_0Perl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Artistic-1.0-Perl.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Artistic-1.0-Perl.json"
    referenceNumber: ClassVar[int] = 600
    longName: ClassVar[str] = "Artistic License 1.0 (Perl)"
    licenseId: ClassVar[str] = "Artistic-1.0-Perl"
    seeAlso: ClassVar[List[str]] = ['http://dev.perl.org/licenses/artistic.html']
    isOsiApproved: ClassVar[bool] = True

class LicenseArtistic2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Artistic-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Artistic-2.0.json"
    referenceNumber: ClassVar[int] = 546
    longName: ClassVar[str] = "Artistic License 2.0"
    licenseId: ClassVar[str] = "Artistic-2.0"
    seeAlso: ClassVar[List[str]] = ['http://www.perlfoundation.org/artistic_license_2_0', 'https://www.perlfoundation.org/artistic-license-20.html', 'https://opensource.org/licenses/artistic-license-2.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseAswfDigitalAssets1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/ASWF-Digital-Assets-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/ASWF-Digital-Assets-1.0.json"
    referenceNumber: ClassVar[int] = 229
    longName: ClassVar[str] = "ASWF Digital Assets License version 1.0"
    licenseId: ClassVar[str] = "ASWF-Digital-Assets-1.0"
    seeAlso: ClassVar[List[str]] = ['https://github.com/AcademySoftwareFoundation/foundation/blob/main/digital_assets/aswf_digital_assets_license_v1.0.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseAswfDigitalAssets1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/ASWF-Digital-Assets-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/ASWF-Digital-Assets-1.1.json"
    referenceNumber: ClassVar[int] = 492
    longName: ClassVar[str] = "ASWF Digital Assets License 1.1"
    licenseId: ClassVar[str] = "ASWF-Digital-Assets-1.1"
    seeAlso: ClassVar[List[str]] = ['https://github.com/AcademySoftwareFoundation/foundation/blob/main/digital_assets/aswf_digital_assets_license_v1.1.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseBaekmuk(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Baekmuk.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Baekmuk.json"
    referenceNumber: ClassVar[int] = 214
    longName: ClassVar[str] = "Baekmuk License"
    licenseId: ClassVar[str] = "Baekmuk"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing:Baekmuk?rd=Licensing/Baekmuk']
    isOsiApproved: ClassVar[bool] = False

class LicenseBahyph(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Bahyph.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Bahyph.json"
    referenceNumber: ClassVar[int] = 432
    longName: ClassVar[str] = "Bahyph License"
    licenseId: ClassVar[str] = "Bahyph"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Bahyph']
    isOsiApproved: ClassVar[bool] = False

class LicenseBarr(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Barr.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Barr.json"
    referenceNumber: ClassVar[int] = 272
    longName: ClassVar[str] = "Barr License"
    licenseId: ClassVar[str] = "Barr"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Barr']
    isOsiApproved: ClassVar[bool] = False

class LicenseBeerware(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Beerware.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Beerware.json"
    referenceNumber: ClassVar[int] = 90
    longName: ClassVar[str] = "Beerware License"
    licenseId: ClassVar[str] = "Beerware"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Beerware', 'https://people.freebsd.org/~phk/']
    isOsiApproved: ClassVar[bool] = False

class LicenseBitstreamCharter(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Bitstream-Charter.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Bitstream-Charter.json"
    referenceNumber: ClassVar[int] = 111
    longName: ClassVar[str] = "Bitstream Charter Font License"
    licenseId: ClassVar[str] = "Bitstream-Charter"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Charter#License_Text', 'https://raw.githubusercontent.com/blackhole89/notekit/master/data/fonts/Charter%20license.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseBitstreamVera(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Bitstream-Vera.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Bitstream-Vera.json"
    referenceNumber: ClassVar[int] = 192
    longName: ClassVar[str] = "Bitstream Vera Font License"
    licenseId: ClassVar[str] = "Bitstream-Vera"
    seeAlso: ClassVar[List[str]] = ['https://web.archive.org/web/20080207013128/http://www.gnome.org/fonts/', 'https://docubrain.com/sites/default/files/licenses/bitstream-vera.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseBittorrent1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BitTorrent-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BitTorrent-1.0.json"
    referenceNumber: ClassVar[int] = 183
    longName: ClassVar[str] = "BitTorrent Open Source License v1.0"
    licenseId: ClassVar[str] = "BitTorrent-1.0"
    seeAlso: ClassVar[List[str]] = ['http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/licenses/BitTorrent?r1=1.1&r2=1.1.1.1&diff_format=s']
    isOsiApproved: ClassVar[bool] = False

class LicenseBittorrent1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BitTorrent-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BitTorrent-1.1.json"
    referenceNumber: ClassVar[int] = 84
    longName: ClassVar[str] = "BitTorrent Open Source License v1.1"
    licenseId: ClassVar[str] = "BitTorrent-1.1"
    seeAlso: ClassVar[List[str]] = ['http://directory.fsf.org/wiki/License:BitTorrentOSL1.1']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseBlessing(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/blessing.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/blessing.json"
    referenceNumber: ClassVar[int] = 50
    longName: ClassVar[str] = "SQLite Blessing"
    licenseId: ClassVar[str] = "blessing"
    seeAlso: ClassVar[List[str]] = ['https://www.sqlite.org/src/artifact/e33a4df7e32d742a?ln=4-9', 'https://sqlite.org/src/artifact/df5091916dbb40e6']
    isOsiApproved: ClassVar[bool] = False

class LicenseBlueoak1_0_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BlueOak-1.0.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BlueOak-1.0.0.json"
    referenceNumber: ClassVar[int] = 366
    longName: ClassVar[str] = "Blue Oak Model License 1.0.0"
    licenseId: ClassVar[str] = "BlueOak-1.0.0"
    seeAlso: ClassVar[List[str]] = ['https://blueoakcouncil.org/license/1.0.0']
    isOsiApproved: ClassVar[bool] = False

class LicenseBoehmGc(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Boehm-GC.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Boehm-GC.json"
    referenceNumber: ClassVar[int] = 343
    longName: ClassVar[str] = "Boehm-Demers-Weiser GC License"
    licenseId: ClassVar[str] = "Boehm-GC"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing:MIT#Another_Minimal_variant_(found_in_libatomic_ops)', 'https://github.com/uim/libgcroots/blob/master/COPYING', 'https://github.com/ivmai/libatomic_ops/blob/master/LICENSE']
    isOsiApproved: ClassVar[bool] = False

class LicenseBorceux(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Borceux.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Borceux.json"
    referenceNumber: ClassVar[int] = 24
    longName: ClassVar[str] = "Borceux license"
    licenseId: ClassVar[str] = "Borceux"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Borceux']
    isOsiApproved: ClassVar[bool] = False

class LicenseBrianGladman3Clause(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Brian-Gladman-3-Clause.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Brian-Gladman-3-Clause.json"
    referenceNumber: ClassVar[int] = 403
    longName: ClassVar[str] = "Brian Gladman 3-Clause License"
    licenseId: ClassVar[str] = "Brian-Gladman-3-Clause"
    seeAlso: ClassVar[List[str]] = ['https://github.com/SWI-Prolog/packages-clib/blob/master/sha1/brg_endian.h']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsd1Clause(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-1-Clause.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-1-Clause.json"
    referenceNumber: ClassVar[int] = 310
    longName: ClassVar[str] = "BSD 1-Clause License"
    licenseId: ClassVar[str] = "BSD-1-Clause"
    seeAlso: ClassVar[List[str]] = ['https://svnweb.freebsd.org/base/head/include/ifaddrs.h?revision=326823']
    isOsiApproved: ClassVar[bool] = True

class LicenseBsd2Clause(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-2-Clause.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-2-Clause.json"
    referenceNumber: ClassVar[int] = 427
    longName: ClassVar[str] = "BSD 2-Clause 'Simplified' License"
    licenseId: ClassVar[str] = "BSD-2-Clause"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/BSD-2-Clause']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseBsd2ClauseFreebsd(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-2-Clause-FreeBSD.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-2-Clause-FreeBSD.json"
    referenceNumber: ClassVar[int] = 507
    longName: ClassVar[str] = "BSD 2-Clause FreeBSD License"
    licenseId: ClassVar[str] = "BSD-2-Clause-FreeBSD"
    seeAlso: ClassVar[List[str]] = ['http://www.freebsd.org/copyright/freebsd-license.html']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseBsd2ClauseNetbsd(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-2-Clause-NetBSD.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-2-Clause-NetBSD.json"
    referenceNumber: ClassVar[int] = 123
    longName: ClassVar[str] = "BSD 2-Clause NetBSD License"
    licenseId: ClassVar[str] = "BSD-2-Clause-NetBSD"
    seeAlso: ClassVar[List[str]] = ['http://www.netbsd.org/about/redistribution.html#default']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseBsd2ClausePatent(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-2-Clause-Patent.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-2-Clause-Patent.json"
    referenceNumber: ClassVar[int] = 12
    longName: ClassVar[str] = "BSD-2-Clause Plus Patent License"
    licenseId: ClassVar[str] = "BSD-2-Clause-Patent"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/BSDplusPatent']
    isOsiApproved: ClassVar[bool] = True

class LicenseBsd2ClauseViews(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-2-Clause-Views.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-2-Clause-Views.json"
    referenceNumber: ClassVar[int] = 25
    longName: ClassVar[str] = "BSD 2-Clause with views sentence"
    licenseId: ClassVar[str] = "BSD-2-Clause-Views"
    seeAlso: ClassVar[List[str]] = ['http://www.freebsd.org/copyright/freebsd-license.html', 'https://people.freebsd.org/~ivoras/wine/patch-wine-nvidia.sh', 'https://github.com/protegeproject/protege/blob/master/license.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsd3Clause(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause.json"
    referenceNumber: ClassVar[int] = 133
    longName: ClassVar[str] = "BSD 3-Clause 'New' or 'Revised' License"
    licenseId: ClassVar[str] = "BSD-3-Clause"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/BSD-3-Clause', 'https://www.eclipse.org/org/documents/edl-v10.php']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseBsd3ClauseAttribution(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-Attribution.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-Attribution.json"
    referenceNumber: ClassVar[int] = 551
    longName: ClassVar[str] = "BSD with attribution"
    licenseId: ClassVar[str] = "BSD-3-Clause-Attribution"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/BSD_with_Attribution']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsd3ClauseClear(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-Clear.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-Clear.json"
    referenceNumber: ClassVar[int] = 465
    longName: ClassVar[str] = "BSD 3-Clause Clear License"
    licenseId: ClassVar[str] = "BSD-3-Clause-Clear"
    seeAlso: ClassVar[List[str]] = ['http://labs.metacarta.com/license-explanation.html#license']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseBsd3ClauseFlex(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-flex.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-flex.json"
    referenceNumber: ClassVar[int] = 450
    longName: ClassVar[str] = "BSD 3-Clause Flex variant"
    licenseId: ClassVar[str] = "BSD-3-Clause-flex"
    seeAlso: ClassVar[List[str]] = ['https://github.com/westes/flex/blob/master/COPYING']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsd3ClauseHp(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-HP.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-HP.json"
    referenceNumber: ClassVar[int] = 120
    longName: ClassVar[str] = "Hewlett-Packard BSD variant license"
    licenseId: ClassVar[str] = "BSD-3-Clause-HP"
    seeAlso: ClassVar[List[str]] = ['https://github.com/zdohnal/hplip/blob/master/COPYING#L939']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsd3ClauseLbnl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-LBNL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-LBNL.json"
    referenceNumber: ClassVar[int] = 245
    longName: ClassVar[str] = "Lawrence Berkeley National Labs BSD variant license"
    licenseId: ClassVar[str] = "BSD-3-Clause-LBNL"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/LBNLBSD']
    isOsiApproved: ClassVar[bool] = True

class LicenseBsd3ClauseModification(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-Modification.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-Modification.json"
    referenceNumber: ClassVar[int] = 368
    longName: ClassVar[str] = "BSD 3-Clause Modification"
    licenseId: ClassVar[str] = "BSD-3-Clause-Modification"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing:BSD#Modification_Variant']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsd3ClauseNoMilitaryLicense(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-No-Military-License.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-No-Military-License.json"
    referenceNumber: ClassVar[int] = 498
    longName: ClassVar[str] = "BSD 3-Clause No Military License"
    licenseId: ClassVar[str] = "BSD-3-Clause-No-Military-License"
    seeAlso: ClassVar[List[str]] = ['https://gitlab.syncad.com/hive/dhive/-/blob/master/LICENSE', 'https://github.com/greymass/swift-eosio/blob/master/LICENSE']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsd3ClauseNoNuclearLicense(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-No-Nuclear-License.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-No-Nuclear-License.json"
    referenceNumber: ClassVar[int] = 249
    longName: ClassVar[str] = "BSD 3-Clause No Nuclear License"
    licenseId: ClassVar[str] = "BSD-3-Clause-No-Nuclear-License"
    seeAlso: ClassVar[List[str]] = ['http://download.oracle.com/otn-pub/java/licenses/bsd.txt?AuthParam=1467140197_43d516ce1776bd08a58235a7785be1cc']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsd3ClauseNoNuclearLicense2014(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-No-Nuclear-License-2014.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-No-Nuclear-License-2014.json"
    referenceNumber: ClassVar[int] = 195
    longName: ClassVar[str] = "BSD 3-Clause No Nuclear License 2014"
    licenseId: ClassVar[str] = "BSD-3-Clause-No-Nuclear-License-2014"
    seeAlso: ClassVar[List[str]] = ['https://java.net/projects/javaeetutorial/pages/BerkeleyLicense']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsd3ClauseNoNuclearWarranty(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-No-Nuclear-Warranty.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-No-Nuclear-Warranty.json"
    referenceNumber: ClassVar[int] = 188
    longName: ClassVar[str] = "BSD 3-Clause No Nuclear Warranty"
    licenseId: ClassVar[str] = "BSD-3-Clause-No-Nuclear-Warranty"
    seeAlso: ClassVar[List[str]] = ['https://jogamp.org/git/?p=gluegen.git;a=blob_plain;f=LICENSE.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsd3ClauseOpenMpi(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-Open-MPI.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-Open-MPI.json"
    referenceNumber: ClassVar[int] = 335
    longName: ClassVar[str] = "BSD 3-Clause Open MPI variant"
    licenseId: ClassVar[str] = "BSD-3-Clause-Open-MPI"
    seeAlso: ClassVar[List[str]] = ['https://www.open-mpi.org/community/license.php', 'http://www.netlib.org/lapack/LICENSE.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsd3ClauseSun(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-Sun.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-3-Clause-Sun.json"
    referenceNumber: ClassVar[int] = 518
    longName: ClassVar[str] = "BSD 3-Clause Sun Microsystems"
    licenseId: ClassVar[str] = "BSD-3-Clause-Sun"
    seeAlso: ClassVar[List[str]] = ['https://github.com/xmlark/msv/blob/b9316e2f2270bc1606952ea4939ec87fbba157f3/xsdlib/src/main/java/com/sun/msv/datatype/regexp/InternalImpl.java']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsd4Clause(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-4-Clause.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-4-Clause.json"
    referenceNumber: ClassVar[int] = 572
    longName: ClassVar[str] = "BSD 4-Clause 'Original' or 'Old' License"
    licenseId: ClassVar[str] = "BSD-4-Clause"
    seeAlso: ClassVar[List[str]] = ['http://directory.fsf.org/wiki/License:BSD_4Clause']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseBsd4ClauseShortened(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-4-Clause-Shortened.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-4-Clause-Shortened.json"
    referenceNumber: ClassVar[int] = 327
    longName: ClassVar[str] = "BSD 4 Clause Shortened"
    licenseId: ClassVar[str] = "BSD-4-Clause-Shortened"
    seeAlso: ClassVar[List[str]] = ['https://metadata.ftp-master.debian.org/changelogs//main/a/arpwatch/arpwatch_2.1a15-7_copyright']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsd4ClauseUc(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-4-Clause-UC.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-4-Clause-UC.json"
    referenceNumber: ClassVar[int] = 160
    longName: ClassVar[str] = "BSD-4-Clause (University of California-Specific)"
    licenseId: ClassVar[str] = "BSD-4-Clause-UC"
    seeAlso: ClassVar[List[str]] = ['http://www.freebsd.org/copyright/license.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsd4_3RENO(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-4.3RENO.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-4.3RENO.json"
    referenceNumber: ClassVar[int] = 560
    longName: ClassVar[str] = "BSD 4.3 RENO License"
    licenseId: ClassVar[str] = "BSD-4.3RENO"
    seeAlso: ClassVar[List[str]] = ['https://sourceware.org/git/?p=binutils-gdb.git;a=blob;f=libiberty/strcasecmp.c;h=131d81c2ce7881fa48c363dc5bf5fb302c61ce0b;hb=HEAD', 'https://git.openldap.org/openldap/openldap/-/blob/master/COPYRIGHT#L55-63']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsd4_3TAHOE(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-4.3TAHOE.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-4.3TAHOE.json"
    referenceNumber: ClassVar[int] = 361
    longName: ClassVar[str] = "BSD 4.3 TAHOE License"
    licenseId: ClassVar[str] = "BSD-4.3TAHOE"
    seeAlso: ClassVar[List[str]] = ['https://github.com/389ds/389-ds-base/blob/main/ldap/include/sysexits-compat.h#L15', 'https://git.savannah.gnu.org/cgit/indent.git/tree/doc/indent.texi?id=a74c6b4ee49397cf330b333da1042bffa60ed14f#n1788']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsdAdvertisingAcknowledgement(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-Advertising-Acknowledgement.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-Advertising-Acknowledgement.json"
    referenceNumber: ClassVar[int] = 31
    longName: ClassVar[str] = "BSD Advertising Acknowledgement License"
    licenseId: ClassVar[str] = "BSD-Advertising-Acknowledgement"
    seeAlso: ClassVar[List[str]] = ['https://github.com/python-excel/xlrd/blob/master/LICENSE#L33']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsdAttributionHpndDisclaimer(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-Attribution-HPND-disclaimer.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-Attribution-HPND-disclaimer.json"
    referenceNumber: ClassVar[int] = 53
    longName: ClassVar[str] = "BSD with Attribution and HPND disclaimer"
    licenseId: ClassVar[str] = "BSD-Attribution-HPND-disclaimer"
    seeAlso: ClassVar[List[str]] = ['https://github.com/cyrusimap/cyrus-sasl/blob/master/COPYING']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsdInfernoNettverk(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-Inferno-Nettverk.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-Inferno-Nettverk.json"
    referenceNumber: ClassVar[int] = 98
    longName: ClassVar[str] = "BSD-Inferno-Nettverk"
    licenseId: ClassVar[str] = "BSD-Inferno-Nettverk"
    seeAlso: ClassVar[List[str]] = ['https://www.inet.no/dante/LICENSE']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsdProtection(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-Protection.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-Protection.json"
    referenceNumber: ClassVar[int] = 281
    longName: ClassVar[str] = "BSD Protection License"
    licenseId: ClassVar[str] = "BSD-Protection"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/BSD_Protection_License']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsdSourceCode(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-Source-Code.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-Source-Code.json"
    referenceNumber: ClassVar[int] = 283
    longName: ClassVar[str] = "BSD Source Code Attribution"
    licenseId: ClassVar[str] = "BSD-Source-Code"
    seeAlso: ClassVar[List[str]] = ['https://github.com/robbiehanson/CocoaHTTPServer/blob/master/LICENSE.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsdSystemics(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSD-Systemics.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSD-Systemics.json"
    referenceNumber: ClassVar[int] = 22
    longName: ClassVar[str] = "Systemics BSD variant license"
    licenseId: ClassVar[str] = "BSD-Systemics"
    seeAlso: ClassVar[List[str]] = ['https://metacpan.org/release/DPARIS/Crypt-DES-2.07/source/COPYRIGHT']
    isOsiApproved: ClassVar[bool] = False

class LicenseBsl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BSL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BSL-1.0.json"
    referenceNumber: ClassVar[int] = 471
    longName: ClassVar[str] = "Boost Software License 1.0"
    licenseId: ClassVar[str] = "BSL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://www.boost.org/LICENSE_1_0.txt', 'https://opensource.org/licenses/BSL-1.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseBusl1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/BUSL-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/BUSL-1.1.json"
    referenceNumber: ClassVar[int] = 424
    longName: ClassVar[str] = "Business Source License 1.1"
    licenseId: ClassVar[str] = "BUSL-1.1"
    seeAlso: ClassVar[List[str]] = ['https://mariadb.com/bsl11/']
    isOsiApproved: ClassVar[bool] = False

class LicenseBzip21_0_5(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/bzip2-1.0.5.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/bzip2-1.0.5.json"
    referenceNumber: ClassVar[int] = 426
    longName: ClassVar[str] = "bzip2 and libbzip2 License v1.0.5"
    licenseId: ClassVar[str] = "bzip2-1.0.5"
    seeAlso: ClassVar[List[str]] = ['https://sourceware.org/bzip2/1.0.5/bzip2-manual-1.0.5.html', 'http://bzip.org/1.0.5/bzip2-manual-1.0.5.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseBzip21_0_6(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/bzip2-1.0.6.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/bzip2-1.0.6.json"
    referenceNumber: ClassVar[int] = 263
    longName: ClassVar[str] = "bzip2 and libbzip2 License v1.0.6"
    licenseId: ClassVar[str] = "bzip2-1.0.6"
    seeAlso: ClassVar[List[str]] = ['https://sourceware.org/git/?p=bzip2.git;a=blob;f=LICENSE;hb=bzip2-1.0.6', 'http://bzip.org/1.0.5/bzip2-manual-1.0.5.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseCUda1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/C-UDA-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/C-UDA-1.0.json"
    referenceNumber: ClassVar[int] = 70
    longName: ClassVar[str] = "Computational Use of Data Agreement v1.0"
    licenseId: ClassVar[str] = "C-UDA-1.0"
    seeAlso: ClassVar[List[str]] = ['https://github.com/microsoft/Computational-Use-of-Data-Agreement/blob/master/C-UDA-1.0.md', 'https://cdla.dev/computational-use-of-data-agreement-v1-0/']
    isOsiApproved: ClassVar[bool] = False

class LicenseCal1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CAL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CAL-1.0.json"
    referenceNumber: ClassVar[int] = 602
    longName: ClassVar[str] = "Cryptographic Autonomy License 1.0"
    licenseId: ClassVar[str] = "CAL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://cryptographicautonomylicense.com/license-text.html', 'https://opensource.org/licenses/CAL-1.0']
    isOsiApproved: ClassVar[bool] = True

class LicenseCal1_0CombinedWorkException(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CAL-1.0-Combined-Work-Exception.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CAL-1.0-Combined-Work-Exception.json"
    referenceNumber: ClassVar[int] = 204
    longName: ClassVar[str] = "Cryptographic Autonomy License 1.0 (Combined Work Exception)"
    licenseId: ClassVar[str] = "CAL-1.0-Combined-Work-Exception"
    seeAlso: ClassVar[List[str]] = ['http://cryptographicautonomylicense.com/license-text.html', 'https://opensource.org/licenses/CAL-1.0']
    isOsiApproved: ClassVar[bool] = True

class LicenseCaldera(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Caldera.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Caldera.json"
    referenceNumber: ClassVar[int] = 309
    longName: ClassVar[str] = "Caldera License"
    licenseId: ClassVar[str] = "Caldera"
    seeAlso: ClassVar[List[str]] = ['http://www.lemis.com/grog/UNIX/ancient-source-all.pdf']
    isOsiApproved: ClassVar[bool] = False

class LicenseCatosl1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CATOSL-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CATOSL-1.1.json"
    referenceNumber: ClassVar[int] = 247
    longName: ClassVar[str] = "Computer Associates Trusted Open Source License 1.1"
    licenseId: ClassVar[str] = "CATOSL-1.1"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/CATOSL-1.1']
    isOsiApproved: ClassVar[bool] = True

class LicenseCcBy1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-1.0.json"
    referenceNumber: ClassVar[int] = 448
    longName: ClassVar[str] = "Creative Commons Attribution 1.0 Generic"
    licenseId: ClassVar[str] = "CC-BY-1.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by/1.0/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcBy2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-2.0.json"
    referenceNumber: ClassVar[int] = 528
    longName: ClassVar[str] = "Creative Commons Attribution 2.0 Generic"
    licenseId: ClassVar[str] = "CC-BY-2.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by/2.0/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcBy2_5(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-2.5.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-2.5.json"
    referenceNumber: ClassVar[int] = 23
    longName: ClassVar[str] = "Creative Commons Attribution 2.5 Generic"
    licenseId: ClassVar[str] = "CC-BY-2.5"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by/2.5/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcBy2_5Au(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-2.5-AU.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-2.5-AU.json"
    referenceNumber: ClassVar[int] = 67
    longName: ClassVar[str] = "Creative Commons Attribution 2.5 Australia"
    licenseId: ClassVar[str] = "CC-BY-2.5-AU"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by/2.5/au/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcBy3_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-3.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-3.0.json"
    referenceNumber: ClassVar[int] = 248
    longName: ClassVar[str] = "Creative Commons Attribution 3.0 Unported"
    licenseId: ClassVar[str] = "CC-BY-3.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by/3.0/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcBy3_0At(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-3.0-AT.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-3.0-AT.json"
    referenceNumber: ClassVar[int] = 468
    longName: ClassVar[str] = "Creative Commons Attribution 3.0 Austria"
    licenseId: ClassVar[str] = "CC-BY-3.0-AT"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by/3.0/at/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcBy3_0De(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-3.0-DE.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-3.0-DE.json"
    referenceNumber: ClassVar[int] = 362
    longName: ClassVar[str] = "Creative Commons Attribution 3.0 Germany"
    licenseId: ClassVar[str] = "CC-BY-3.0-DE"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by/3.0/de/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcBy3_0Igo(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-3.0-IGO.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-3.0-IGO.json"
    referenceNumber: ClassVar[int] = 298
    longName: ClassVar[str] = "Creative Commons Attribution 3.0 IGO"
    licenseId: ClassVar[str] = "CC-BY-3.0-IGO"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by/3.0/igo/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcBy3_0Nl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-3.0-NL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-3.0-NL.json"
    referenceNumber: ClassVar[int] = 315
    longName: ClassVar[str] = "Creative Commons Attribution 3.0 Netherlands"
    licenseId: ClassVar[str] = "CC-BY-3.0-NL"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by/3.0/nl/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcBy3_0Us(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-3.0-US.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-3.0-US.json"
    referenceNumber: ClassVar[int] = 83
    longName: ClassVar[str] = "Creative Commons Attribution 3.0 United States"
    licenseId: ClassVar[str] = "CC-BY-3.0-US"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by/3.0/us/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcBy4_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-4.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-4.0.json"
    referenceNumber: ClassVar[int] = 80
    longName: ClassVar[str] = "Creative Commons Attribution 4.0 International"
    licenseId: ClassVar[str] = "CC-BY-4.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by/4.0/legalcode']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseCcByNc1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-1.0.json"
    referenceNumber: ClassVar[int] = 54
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial 1.0 Generic"
    licenseId: ClassVar[str] = "CC-BY-NC-1.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc/1.0/legalcode']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = False

class LicenseCcByNc2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-2.0.json"
    referenceNumber: ClassVar[int] = 7
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial 2.0 Generic"
    licenseId: ClassVar[str] = "CC-BY-NC-2.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc/2.0/legalcode']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = False

class LicenseCcByNc2_5(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-2.5.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-2.5.json"
    referenceNumber: ClassVar[int] = 596
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial 2.5 Generic"
    licenseId: ClassVar[str] = "CC-BY-NC-2.5"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc/2.5/legalcode']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = False

class LicenseCcByNc3_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-3.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-3.0.json"
    referenceNumber: ClassVar[int] = 322
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial 3.0 Unported"
    licenseId: ClassVar[str] = "CC-BY-NC-3.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc/3.0/legalcode']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = False

class LicenseCcByNc3_0De(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-3.0-DE.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-3.0-DE.json"
    referenceNumber: ClassVar[int] = 261
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial 3.0 Germany"
    licenseId: ClassVar[str] = "CC-BY-NC-3.0-DE"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc/3.0/de/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcByNc4_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-4.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-4.0.json"
    referenceNumber: ClassVar[int] = 266
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial 4.0 International"
    licenseId: ClassVar[str] = "CC-BY-NC-4.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc/4.0/legalcode']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = False

class LicenseCcByNcNd1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-ND-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-ND-1.0.json"
    referenceNumber: ClassVar[int] = 280
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial No Derivatives 1.0 Generic"
    licenseId: ClassVar[str] = "CC-BY-NC-ND-1.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nd-nc/1.0/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcByNcNd2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-ND-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-ND-2.0.json"
    referenceNumber: ClassVar[int] = 581
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial No Derivatives 2.0 Generic"
    licenseId: ClassVar[str] = "CC-BY-NC-ND-2.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc-nd/2.0/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcByNcNd2_5(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-ND-2.5.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-ND-2.5.json"
    referenceNumber: ClassVar[int] = 73
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial No Derivatives 2.5 Generic"
    licenseId: ClassVar[str] = "CC-BY-NC-ND-2.5"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc-nd/2.5/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcByNcNd3_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-ND-3.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-ND-3.0.json"
    referenceNumber: ClassVar[int] = 86
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial No Derivatives 3.0 Unported"
    licenseId: ClassVar[str] = "CC-BY-NC-ND-3.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc-nd/3.0/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcByNcNd3_0De(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-ND-3.0-DE.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-ND-3.0-DE.json"
    referenceNumber: ClassVar[int] = 435
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial No Derivatives 3.0 Germany"
    licenseId: ClassVar[str] = "CC-BY-NC-ND-3.0-DE"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc-nd/3.0/de/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcByNcNd3_0Igo(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-ND-3.0-IGO.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-ND-3.0-IGO.json"
    referenceNumber: ClassVar[int] = 117
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial No Derivatives 3.0 IGO"
    licenseId: ClassVar[str] = "CC-BY-NC-ND-3.0-IGO"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc-nd/3.0/igo/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcByNcNd4_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-ND-4.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-ND-4.0.json"
    referenceNumber: ClassVar[int] = 463
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial No Derivatives 4.0 International"
    licenseId: ClassVar[str] = "CC-BY-NC-ND-4.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcByNcSa1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-1.0.json"
    referenceNumber: ClassVar[int] = 594
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial Share Alike 1.0 Generic"
    licenseId: ClassVar[str] = "CC-BY-NC-SA-1.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc-sa/1.0/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcByNcSa2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-2.0.json"
    referenceNumber: ClassVar[int] = 196
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial Share Alike 2.0 Generic"
    licenseId: ClassVar[str] = "CC-BY-NC-SA-2.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc-sa/2.0/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcByNcSa2_0De(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-2.0-DE.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-2.0-DE.json"
    referenceNumber: ClassVar[int] = 316
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial Share Alike 2.0 Germany"
    licenseId: ClassVar[str] = "CC-BY-NC-SA-2.0-DE"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc-sa/2.0/de/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcByNcSa2_0Fr(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-2.0-FR.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-2.0-FR.json"
    referenceNumber: ClassVar[int] = 75
    longName: ClassVar[str] = "Creative Commons Attribution-NonCommercial-ShareAlike 2.0 France"
    licenseId: ClassVar[str] = "CC-BY-NC-SA-2.0-FR"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc-sa/2.0/fr/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcByNcSa2_0Uk(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-2.0-UK.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-2.0-UK.json"
    referenceNumber: ClassVar[int] = 42
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial Share Alike 2.0 England and Wales"
    licenseId: ClassVar[str] = "CC-BY-NC-SA-2.0-UK"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc-sa/2.0/uk/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcByNcSa2_5(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-2.5.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-2.5.json"
    referenceNumber: ClassVar[int] = 55
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial Share Alike 2.5 Generic"
    licenseId: ClassVar[str] = "CC-BY-NC-SA-2.5"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc-sa/2.5/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcByNcSa3_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-3.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-3.0.json"
    referenceNumber: ClassVar[int] = 233
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial Share Alike 3.0 Unported"
    licenseId: ClassVar[str] = "CC-BY-NC-SA-3.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc-sa/3.0/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcByNcSa3_0De(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-3.0-DE.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-3.0-DE.json"
    referenceNumber: ClassVar[int] = 236
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial Share Alike 3.0 Germany"
    licenseId: ClassVar[str] = "CC-BY-NC-SA-3.0-DE"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc-sa/3.0/de/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcByNcSa3_0Igo(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-3.0-IGO.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-3.0-IGO.json"
    referenceNumber: ClassVar[int] = 313
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial Share Alike 3.0 IGO"
    licenseId: ClassVar[str] = "CC-BY-NC-SA-3.0-IGO"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc-sa/3.0/igo/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcByNcSa4_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-4.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-NC-SA-4.0.json"
    referenceNumber: ClassVar[int] = 583
    longName: ClassVar[str] = "Creative Commons Attribution Non Commercial Share Alike 4.0 International"
    licenseId: ClassVar[str] = "CC-BY-NC-SA-4.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcByNd1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-ND-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-ND-1.0.json"
    referenceNumber: ClassVar[int] = 453
    longName: ClassVar[str] = "Creative Commons Attribution No Derivatives 1.0 Generic"
    licenseId: ClassVar[str] = "CC-BY-ND-1.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nd/1.0/legalcode']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = False

class LicenseCcByNd2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-ND-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-ND-2.0.json"
    referenceNumber: ClassVar[int] = 473
    longName: ClassVar[str] = "Creative Commons Attribution No Derivatives 2.0 Generic"
    licenseId: ClassVar[str] = "CC-BY-ND-2.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nd/2.0/legalcode']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = False

class LicenseCcByNd2_5(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-ND-2.5.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-ND-2.5.json"
    referenceNumber: ClassVar[int] = 425
    longName: ClassVar[str] = "Creative Commons Attribution No Derivatives 2.5 Generic"
    licenseId: ClassVar[str] = "CC-BY-ND-2.5"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nd/2.5/legalcode']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = False

class LicenseCcByNd3_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-ND-3.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-ND-3.0.json"
    referenceNumber: ClassVar[int] = 333
    longName: ClassVar[str] = "Creative Commons Attribution No Derivatives 3.0 Unported"
    licenseId: ClassVar[str] = "CC-BY-ND-3.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nd/3.0/legalcode']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = False

class LicenseCcByNd3_0De(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-ND-3.0-DE.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-ND-3.0-DE.json"
    referenceNumber: ClassVar[int] = 467
    longName: ClassVar[str] = "Creative Commons Attribution No Derivatives 3.0 Germany"
    licenseId: ClassVar[str] = "CC-BY-ND-3.0-DE"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nd/3.0/de/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcByNd4_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-ND-4.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-ND-4.0.json"
    referenceNumber: ClassVar[int] = 388
    longName: ClassVar[str] = "Creative Commons Attribution No Derivatives 4.0 International"
    licenseId: ClassVar[str] = "CC-BY-ND-4.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-nd/4.0/legalcode']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = False

class LicenseCcBySa1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-1.0.json"
    referenceNumber: ClassVar[int] = 457
    longName: ClassVar[str] = "Creative Commons Attribution Share Alike 1.0 Generic"
    licenseId: ClassVar[str] = "CC-BY-SA-1.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-sa/1.0/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcBySa2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-2.0.json"
    referenceNumber: ClassVar[int] = 408
    longName: ClassVar[str] = "Creative Commons Attribution Share Alike 2.0 Generic"
    licenseId: ClassVar[str] = "CC-BY-SA-2.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-sa/2.0/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcBySa2_0Uk(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-2.0-UK.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-2.0-UK.json"
    referenceNumber: ClassVar[int] = 276
    longName: ClassVar[str] = "Creative Commons Attribution Share Alike 2.0 England and Wales"
    licenseId: ClassVar[str] = "CC-BY-SA-2.0-UK"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-sa/2.0/uk/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcBySa2_1Jp(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-2.1-JP.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-2.1-JP.json"
    referenceNumber: ClassVar[int] = 287
    longName: ClassVar[str] = "Creative Commons Attribution Share Alike 2.1 Japan"
    licenseId: ClassVar[str] = "CC-BY-SA-2.1-JP"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-sa/2.1/jp/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcBySa2_5(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-2.5.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-2.5.json"
    referenceNumber: ClassVar[int] = 352
    longName: ClassVar[str] = "Creative Commons Attribution Share Alike 2.5 Generic"
    licenseId: ClassVar[str] = "CC-BY-SA-2.5"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-sa/2.5/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcBySa3_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-3.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-3.0.json"
    referenceNumber: ClassVar[int] = 527
    longName: ClassVar[str] = "Creative Commons Attribution Share Alike 3.0 Unported"
    licenseId: ClassVar[str] = "CC-BY-SA-3.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-sa/3.0/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcBySa3_0At(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-3.0-AT.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-3.0-AT.json"
    referenceNumber: ClassVar[int] = 529
    longName: ClassVar[str] = "Creative Commons Attribution Share Alike 3.0 Austria"
    licenseId: ClassVar[str] = "CC-BY-SA-3.0-AT"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-sa/3.0/at/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcBySa3_0De(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-3.0-DE.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-3.0-DE.json"
    referenceNumber: ClassVar[int] = 446
    longName: ClassVar[str] = "Creative Commons Attribution Share Alike 3.0 Germany"
    licenseId: ClassVar[str] = "CC-BY-SA-3.0-DE"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-sa/3.0/de/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcBySa3_0Igo(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-3.0-IGO.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-3.0-IGO.json"
    referenceNumber: ClassVar[int] = 44
    longName: ClassVar[str] = "Creative Commons Attribution-ShareAlike 3.0 IGO"
    licenseId: ClassVar[str] = "CC-BY-SA-3.0-IGO"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-sa/3.0/igo/legalcode']
    isOsiApproved: ClassVar[bool] = False

class LicenseCcBySa4_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-4.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-BY-SA-4.0.json"
    referenceNumber: ClassVar[int] = 197
    longName: ClassVar[str] = "Creative Commons Attribution Share Alike 4.0 International"
    licenseId: ClassVar[str] = "CC-BY-SA-4.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/by-sa/4.0/legalcode']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseCcPddc(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC-PDDC.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC-PDDC.json"
    referenceNumber: ClassVar[int] = 88
    longName: ClassVar[str] = "Creative Commons Public Domain Dedication and Certification"
    licenseId: ClassVar[str] = "CC-PDDC"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/licenses/publicdomain/']
    isOsiApproved: ClassVar[bool] = False

class LicenseCc01_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CC0-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CC0-1.0.json"
    referenceNumber: ClassVar[int] = 87
    longName: ClassVar[str] = "Creative Commons Zero v1.0 Universal"
    licenseId: ClassVar[str] = "CC0-1.0"
    seeAlso: ClassVar[List[str]] = ['https://creativecommons.org/publicdomain/zero/1.0/legalcode']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseCddl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CDDL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CDDL-1.0.json"
    referenceNumber: ClassVar[int] = 451
    longName: ClassVar[str] = "Common Development and Distribution License 1.0"
    licenseId: ClassVar[str] = "CDDL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/cddl1']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseCddl1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CDDL-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CDDL-1.1.json"
    referenceNumber: ClassVar[int] = 156
    longName: ClassVar[str] = "Common Development and Distribution License 1.1"
    licenseId: ClassVar[str] = "CDDL-1.1"
    seeAlso: ClassVar[List[str]] = ['http://glassfish.java.net/public/CDDL+GPL_1_1.html', 'https://javaee.github.io/glassfish/LICENSE']
    isOsiApproved: ClassVar[bool] = False

class LicenseCdl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CDL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CDL-1.0.json"
    referenceNumber: ClassVar[int] = 524
    longName: ClassVar[str] = "Common Documentation License 1.0"
    licenseId: ClassVar[str] = "CDL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://www.opensource.apple.com/cdl/', 'https://fedoraproject.org/wiki/Licensing/Common_Documentation_License', 'https://www.gnu.org/licenses/license-list.html#ACDL']
    isOsiApproved: ClassVar[bool] = False

class LicenseCdlaPermissive1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CDLA-Permissive-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CDLA-Permissive-1.0.json"
    referenceNumber: ClassVar[int] = 85
    longName: ClassVar[str] = "Community Data License Agreement Permissive 1.0"
    licenseId: ClassVar[str] = "CDLA-Permissive-1.0"
    seeAlso: ClassVar[List[str]] = ['https://cdla.io/permissive-1-0']
    isOsiApproved: ClassVar[bool] = False

class LicenseCdlaPermissive2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CDLA-Permissive-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CDLA-Permissive-2.0.json"
    referenceNumber: ClassVar[int] = 493
    longName: ClassVar[str] = "Community Data License Agreement Permissive 2.0"
    licenseId: ClassVar[str] = "CDLA-Permissive-2.0"
    seeAlso: ClassVar[List[str]] = ['https://cdla.dev/permissive-2-0']
    isOsiApproved: ClassVar[bool] = False

class LicenseCdlaSharing1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CDLA-Sharing-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CDLA-Sharing-1.0.json"
    referenceNumber: ClassVar[int] = 198
    longName: ClassVar[str] = "Community Data License Agreement Sharing 1.0"
    licenseId: ClassVar[str] = "CDLA-Sharing-1.0"
    seeAlso: ClassVar[List[str]] = ['https://cdla.io/sharing-1-0']
    isOsiApproved: ClassVar[bool] = False

class LicenseCecill1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CECILL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CECILL-1.0.json"
    referenceNumber: ClassVar[int] = 430
    longName: ClassVar[str] = "CeCILL Free Software License Agreement v1.0"
    licenseId: ClassVar[str] = "CECILL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://www.cecill.info/licences/Licence_CeCILL_V1-fr.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseCecill1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CECILL-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CECILL-1.1.json"
    referenceNumber: ClassVar[int] = 419
    longName: ClassVar[str] = "CeCILL Free Software License Agreement v1.1"
    licenseId: ClassVar[str] = "CECILL-1.1"
    seeAlso: ClassVar[List[str]] = ['http://www.cecill.info/licences/Licence_CeCILL_V1.1-US.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseCecill2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CECILL-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CECILL-2.0.json"
    referenceNumber: ClassVar[int] = 131
    longName: ClassVar[str] = "CeCILL Free Software License Agreement v2.0"
    licenseId: ClassVar[str] = "CECILL-2.0"
    seeAlso: ClassVar[List[str]] = ['http://www.cecill.info/licences/Licence_CeCILL_V2-en.html']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseCecill2_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CECILL-2.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CECILL-2.1.json"
    referenceNumber: ClassVar[int] = 339
    longName: ClassVar[str] = "CeCILL Free Software License Agreement v2.1"
    licenseId: ClassVar[str] = "CECILL-2.1"
    seeAlso: ClassVar[List[str]] = ['http://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html']
    isOsiApproved: ClassVar[bool] = True

class LicenseCecillB(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CECILL-B.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CECILL-B.json"
    referenceNumber: ClassVar[int] = 411
    longName: ClassVar[str] = "CeCILL-B Free Software License Agreement"
    licenseId: ClassVar[str] = "CECILL-B"
    seeAlso: ClassVar[List[str]] = ['http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseCecillC(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CECILL-C.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CECILL-C.json"
    referenceNumber: ClassVar[int] = 66
    longName: ClassVar[str] = "CeCILL-C Free Software License Agreement"
    licenseId: ClassVar[str] = "CECILL-C"
    seeAlso: ClassVar[List[str]] = ['http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseCernOhl1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CERN-OHL-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CERN-OHL-1.1.json"
    referenceNumber: ClassVar[int] = 447
    longName: ClassVar[str] = "CERN Open Hardware Licence v1.1"
    licenseId: ClassVar[str] = "CERN-OHL-1.1"
    seeAlso: ClassVar[List[str]] = ['https://www.ohwr.org/project/licenses/wikis/cern-ohl-v1.1']
    isOsiApproved: ClassVar[bool] = False

class LicenseCernOhl1_2(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CERN-OHL-1.2.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CERN-OHL-1.2.json"
    referenceNumber: ClassVar[int] = 238
    longName: ClassVar[str] = "CERN Open Hardware Licence v1.2"
    licenseId: ClassVar[str] = "CERN-OHL-1.2"
    seeAlso: ClassVar[List[str]] = ['https://www.ohwr.org/project/licenses/wikis/cern-ohl-v1.2']
    isOsiApproved: ClassVar[bool] = False

class LicenseCernOhlP2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CERN-OHL-P-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CERN-OHL-P-2.0.json"
    referenceNumber: ClassVar[int] = 470
    longName: ClassVar[str] = "CERN Open Hardware Licence Version 2 - Permissive"
    licenseId: ClassVar[str] = "CERN-OHL-P-2.0"
    seeAlso: ClassVar[List[str]] = ['https://www.ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2']
    isOsiApproved: ClassVar[bool] = True

class LicenseCernOhlS2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CERN-OHL-S-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CERN-OHL-S-2.0.json"
    referenceNumber: ClassVar[int] = 328
    longName: ClassVar[str] = "CERN Open Hardware Licence Version 2 - Strongly Reciprocal"
    licenseId: ClassVar[str] = "CERN-OHL-S-2.0"
    seeAlso: ClassVar[List[str]] = ['https://www.ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2']
    isOsiApproved: ClassVar[bool] = True

class LicenseCernOhlW2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CERN-OHL-W-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CERN-OHL-W-2.0.json"
    referenceNumber: ClassVar[int] = 252
    longName: ClassVar[str] = "CERN Open Hardware Licence Version 2 - Weakly Reciprocal"
    licenseId: ClassVar[str] = "CERN-OHL-W-2.0"
    seeAlso: ClassVar[List[str]] = ['https://www.ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2']
    isOsiApproved: ClassVar[bool] = True

class LicenseCfitsio(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CFITSIO.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CFITSIO.json"
    referenceNumber: ClassVar[int] = 319
    longName: ClassVar[str] = "CFITSIO License"
    licenseId: ClassVar[str] = "CFITSIO"
    seeAlso: ClassVar[List[str]] = ['https://heasarc.gsfc.nasa.gov/docs/software/fitsio/c/f_user/node9.html', 'https://heasarc.gsfc.nasa.gov/docs/software/ftools/fv/doc/license.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseCheckCvs(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/check-cvs.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/check-cvs.json"
    referenceNumber: ClassVar[int] = 191
    longName: ClassVar[str] = "check-cvs License"
    licenseId: ClassVar[str] = "check-cvs"
    seeAlso: ClassVar[List[str]] = ['http://cvs.savannah.gnu.org/viewvc/cvs/ccvs/contrib/check_cvs.in?revision=1.1.4.3&view=markup&pathrev=cvs1-11-23#l2']
    isOsiApproved: ClassVar[bool] = False

class LicenseCheckmk(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/checkmk.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/checkmk.json"
    referenceNumber: ClassVar[int] = 422
    longName: ClassVar[str] = "Checkmk License"
    licenseId: ClassVar[str] = "checkmk"
    seeAlso: ClassVar[List[str]] = ['https://github.com/libcheck/check/blob/master/checkmk/checkmk.in']
    isOsiApproved: ClassVar[bool] = False

class LicenseClartistic(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/ClArtistic.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/ClArtistic.json"
    referenceNumber: ClassVar[int] = 253
    longName: ClassVar[str] = "Clarified Artistic License"
    licenseId: ClassVar[str] = "ClArtistic"
    seeAlso: ClassVar[List[str]] = ['http://gianluca.dellavedova.org/2011/01/03/clarified-artistic-license/', 'http://www.ncftp.com/ncftp/doc/LICENSE.txt']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseClips(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Clips.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Clips.json"
    referenceNumber: ClassVar[int] = 520
    longName: ClassVar[str] = "Clips License"
    licenseId: ClassVar[str] = "Clips"
    seeAlso: ClassVar[List[str]] = ['https://github.com/DrItanium/maya/blob/master/LICENSE.CLIPS']
    isOsiApproved: ClassVar[bool] = False

class LicenseCmuMach(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CMU-Mach.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CMU-Mach.json"
    referenceNumber: ClassVar[int] = 484
    longName: ClassVar[str] = "CMU Mach License"
    licenseId: ClassVar[str] = "CMU-Mach"
    seeAlso: ClassVar[List[str]] = ['https://www.cs.cmu.edu/~410/licenses.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseCnriJython(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CNRI-Jython.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CNRI-Jython.json"
    referenceNumber: ClassVar[int] = 82
    longName: ClassVar[str] = "CNRI Jython License"
    licenseId: ClassVar[str] = "CNRI-Jython"
    seeAlso: ClassVar[List[str]] = ['http://www.jython.org/license.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseCnriPython(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CNRI-Python.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CNRI-Python.json"
    referenceNumber: ClassVar[int] = 11
    longName: ClassVar[str] = "CNRI Python License"
    licenseId: ClassVar[str] = "CNRI-Python"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/CNRI-Python']
    isOsiApproved: ClassVar[bool] = True

class LicenseCnriPythonGplCompatible(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CNRI-Python-GPL-Compatible.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CNRI-Python-GPL-Compatible.json"
    referenceNumber: ClassVar[int] = 582
    longName: ClassVar[str] = "CNRI Python Open Source GPL Compatible License Agreement"
    licenseId: ClassVar[str] = "CNRI-Python-GPL-Compatible"
    seeAlso: ClassVar[List[str]] = ['http://www.python.org/download/releases/1.6.1/download_win/']
    isOsiApproved: ClassVar[bool] = False

class LicenseCoil1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/COIL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/COIL-1.0.json"
    referenceNumber: ClassVar[int] = 538
    longName: ClassVar[str] = "Copyfree Open Innovation License"
    licenseId: ClassVar[str] = "COIL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://coil.apotheon.org/plaintext/01.0.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseCommunitySpec1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Community-Spec-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Community-Spec-1.0.json"
    referenceNumber: ClassVar[int] = 185
    longName: ClassVar[str] = "Community Specification License 1.0"
    licenseId: ClassVar[str] = "Community-Spec-1.0"
    seeAlso: ClassVar[List[str]] = ['https://github.com/CommunitySpecification/1.0/blob/master/1._Community_Specification_License-v1.md']
    isOsiApproved: ClassVar[bool] = False

class LicenseCondor1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Condor-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Condor-1.1.json"
    referenceNumber: ClassVar[int] = 270
    longName: ClassVar[str] = "Condor Public License v1.1"
    licenseId: ClassVar[str] = "Condor-1.1"
    seeAlso: ClassVar[List[str]] = ['http://research.cs.wisc.edu/condor/license.html#condor', 'http://web.archive.org/web/20111123062036/http://research.cs.wisc.edu/condor/license.html#condor']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseCopyleftNext0_3_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/copyleft-next-0.3.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/copyleft-next-0.3.0.json"
    referenceNumber: ClassVar[int] = 62
    longName: ClassVar[str] = "copyleft-next 0.3.0"
    licenseId: ClassVar[str] = "copyleft-next-0.3.0"
    seeAlso: ClassVar[List[str]] = ['https://github.com/copyleft-next/copyleft-next/blob/master/Releases/copyleft-next-0.3.0']
    isOsiApproved: ClassVar[bool] = False

class LicenseCopyleftNext0_3_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/copyleft-next-0.3.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/copyleft-next-0.3.1.json"
    referenceNumber: ClassVar[int] = 92
    longName: ClassVar[str] = "copyleft-next 0.3.1"
    licenseId: ClassVar[str] = "copyleft-next-0.3.1"
    seeAlso: ClassVar[List[str]] = ['https://github.com/copyleft-next/copyleft-next/blob/master/Releases/copyleft-next-0.3.1']
    isOsiApproved: ClassVar[bool] = False

class LicenseCornellLosslessJpeg(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Cornell-Lossless-JPEG.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Cornell-Lossless-JPEG.json"
    referenceNumber: ClassVar[int] = 89
    longName: ClassVar[str] = "Cornell Lossless JPEG License"
    licenseId: ClassVar[str] = "Cornell-Lossless-JPEG"
    seeAlso: ClassVar[List[str]] = ['https://android.googlesource.com/platform/external/dng_sdk/+/refs/heads/master/source/dng_lossless_jpeg.cpp#16', 'https://www.mssl.ucl.ac.uk/~mcrw/src/20050920/proto.h', 'https://gitlab.freedesktop.org/libopenraw/libopenraw/blob/master/lib/ljpegdecompressor.cpp#L32']
    isOsiApproved: ClassVar[bool] = False

class LicenseCpal1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CPAL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CPAL-1.0.json"
    referenceNumber: ClassVar[int] = 110
    longName: ClassVar[str] = "Common Public Attribution License 1.0"
    licenseId: ClassVar[str] = "CPAL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/CPAL-1.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseCpl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CPL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CPL-1.0.json"
    referenceNumber: ClassVar[int] = 566
    longName: ClassVar[str] = "Common Public License 1.0"
    licenseId: ClassVar[str] = "CPL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/CPL-1.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseCpol1_02(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CPOL-1.02.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CPOL-1.02.json"
    referenceNumber: ClassVar[int] = 573
    longName: ClassVar[str] = "Code Project Open License 1.02"
    licenseId: ClassVar[str] = "CPOL-1.02"
    seeAlso: ClassVar[List[str]] = ['http://www.codeproject.com/info/cpol10.aspx']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = False

class LicenseCronyx(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Cronyx.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Cronyx.json"
    referenceNumber: ClassVar[int] = 209
    longName: ClassVar[str] = "Cronyx License"
    licenseId: ClassVar[str] = "Cronyx"
    seeAlso: ClassVar[List[str]] = ['https://gitlab.freedesktop.org/xorg/font/alias/-/blob/master/COPYING', 'https://gitlab.freedesktop.org/xorg/font/cronyx-cyrillic/-/blob/master/COPYING', 'https://gitlab.freedesktop.org/xorg/font/misc-cyrillic/-/blob/master/COPYING', 'https://gitlab.freedesktop.org/xorg/font/screen-cyrillic/-/blob/master/COPYING']
    isOsiApproved: ClassVar[bool] = False

class LicenseCrossword(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Crossword.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Crossword.json"
    referenceNumber: ClassVar[int] = 592
    longName: ClassVar[str] = "Crossword License"
    licenseId: ClassVar[str] = "Crossword"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Crossword']
    isOsiApproved: ClassVar[bool] = False

class LicenseCrystalstacker(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CrystalStacker.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CrystalStacker.json"
    referenceNumber: ClassVar[int] = 216
    longName: ClassVar[str] = "CrystalStacker License"
    licenseId: ClassVar[str] = "CrystalStacker"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing:CrystalStacker?rd=Licensing/CrystalStacker']
    isOsiApproved: ClassVar[bool] = False

class LicenseCuaOpl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/CUA-OPL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/CUA-OPL-1.0.json"
    referenceNumber: ClassVar[int] = 97
    longName: ClassVar[str] = "CUA Office Public License v1.0"
    licenseId: ClassVar[str] = "CUA-OPL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/CUA-OPL-1.0']
    isOsiApproved: ClassVar[bool] = True

class LicenseCube(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Cube.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Cube.json"
    referenceNumber: ClassVar[int] = 501
    longName: ClassVar[str] = "Cube License"
    licenseId: ClassVar[str] = "Cube"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Cube']
    isOsiApproved: ClassVar[bool] = False

class LicenseCurl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/curl.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/curl.json"
    referenceNumber: ClassVar[int] = 537
    longName: ClassVar[str] = "curl License"
    licenseId: ClassVar[str] = "curl"
    seeAlso: ClassVar[List[str]] = ['https://github.com/bagder/curl/blob/master/COPYING']
    isOsiApproved: ClassVar[bool] = False

class LicenseDFsl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/D-FSL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/D-FSL-1.0.json"
    referenceNumber: ClassVar[int] = 456
    longName: ClassVar[str] = "Deutsche Freie Software Lizenz"
    licenseId: ClassVar[str] = "D-FSL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://www.dipp.nrw.de/d-fsl/lizenzen/', 'http://www.dipp.nrw.de/d-fsl/index_html/lizenzen/de/D-FSL-1_0_de.txt', 'http://www.dipp.nrw.de/d-fsl/index_html/lizenzen/en/D-FSL-1_0_en.txt', 'https://www.hbz-nrw.de/produkte/open-access/lizenzen/dfsl', 'https://www.hbz-nrw.de/produkte/open-access/lizenzen/dfsl/deutsche-freie-software-lizenz', 'https://www.hbz-nrw.de/produkte/open-access/lizenzen/dfsl/german-free-software-license', 'https://www.hbz-nrw.de/produkte/open-access/lizenzen/dfsl/D-FSL-1_0_de.txt/at_download/file', 'https://www.hbz-nrw.de/produkte/open-access/lizenzen/dfsl/D-FSL-1_0_en.txt/at_download/file']
    isOsiApproved: ClassVar[bool] = False

class LicenseDec3Clause(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/DEC-3-Clause.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/DEC-3-Clause.json"
    referenceNumber: ClassVar[int] = 508
    longName: ClassVar[str] = "DEC 3-Clause License"
    licenseId: ClassVar[str] = "DEC-3-Clause"
    seeAlso: ClassVar[List[str]] = ['https://gitlab.freedesktop.org/xorg/xserver/-/blob/master/COPYING?ref_type=heads#L239']
    isOsiApproved: ClassVar[bool] = False

class LicenseDiffmark(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/diffmark.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/diffmark.json"
    referenceNumber: ClassVar[int] = 331
    longName: ClassVar[str] = "diffmark license"
    licenseId: ClassVar[str] = "diffmark"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/diffmark']
    isOsiApproved: ClassVar[bool] = False

class LicenseDlDeBy2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/DL-DE-BY-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/DL-DE-BY-2.0.json"
    referenceNumber: ClassVar[int] = 500
    longName: ClassVar[str] = "Data licence Germany – attribution – version 2.0"
    licenseId: ClassVar[str] = "DL-DE-BY-2.0"
    seeAlso: ClassVar[List[str]] = ['https://www.govdata.de/dl-de/by-2-0']
    isOsiApproved: ClassVar[bool] = False

class LicenseDlDeZero2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/DL-DE-ZERO-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/DL-DE-ZERO-2.0.json"
    referenceNumber: ClassVar[int] = 407
    longName: ClassVar[str] = "Data licence Germany – zero – version 2.0"
    licenseId: ClassVar[str] = "DL-DE-ZERO-2.0"
    seeAlso: ClassVar[List[str]] = ['https://www.govdata.de/dl-de/zero-2-0']
    isOsiApproved: ClassVar[bool] = False

class LicenseDoc(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/DOC.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/DOC.json"
    referenceNumber: ClassVar[int] = 79
    longName: ClassVar[str] = "DOC License"
    licenseId: ClassVar[str] = "DOC"
    seeAlso: ClassVar[List[str]] = ['http://www.cs.wustl.edu/~schmidt/ACE-copying.html', 'https://www.dre.vanderbilt.edu/~schmidt/ACE-copying.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseDotseqn(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Dotseqn.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Dotseqn.json"
    referenceNumber: ClassVar[int] = 255
    longName: ClassVar[str] = "Dotseqn License"
    licenseId: ClassVar[str] = "Dotseqn"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Dotseqn']
    isOsiApproved: ClassVar[bool] = False

class LicenseDrl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/DRL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/DRL-1.0.json"
    referenceNumber: ClassVar[int] = 284
    longName: ClassVar[str] = "Detection Rule License 1.0"
    licenseId: ClassVar[str] = "DRL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://github.com/Neo23x0/sigma/blob/master/LICENSE.Detection.Rules.md']
    isOsiApproved: ClassVar[bool] = False

class LicenseDrl1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/DRL-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/DRL-1.1.json"
    referenceNumber: ClassVar[int] = 203
    longName: ClassVar[str] = "Detection Rule License 1.1"
    licenseId: ClassVar[str] = "DRL-1.1"
    seeAlso: ClassVar[List[str]] = ['https://github.com/SigmaHQ/Detection-Rule-License/blob/6ec7fbde6101d101b5b5d1fcb8f9b69fbc76c04a/LICENSE.Detection.Rules.md']
    isOsiApproved: ClassVar[bool] = False

class LicenseDsdp(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/DSDP.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/DSDP.json"
    referenceNumber: ClassVar[int] = 137
    longName: ClassVar[str] = "DSDP License"
    licenseId: ClassVar[str] = "DSDP"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/DSDP']
    isOsiApproved: ClassVar[bool] = False

class LicenseDtoa(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/dtoa.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/dtoa.json"
    referenceNumber: ClassVar[int] = 386
    longName: ClassVar[str] = "David M. Gay dtoa License"
    licenseId: ClassVar[str] = "dtoa"
    seeAlso: ClassVar[List[str]] = ['https://github.com/SWI-Prolog/swipl-devel/blob/master/src/os/dtoa.c']
    isOsiApproved: ClassVar[bool] = False

class LicenseDvipdfm(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/dvipdfm.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/dvipdfm.json"
    referenceNumber: ClassVar[int] = 124
    longName: ClassVar[str] = "dvipdfm License"
    licenseId: ClassVar[str] = "dvipdfm"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/dvipdfm']
    isOsiApproved: ClassVar[bool] = False

class LicenseEcl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/ECL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/ECL-1.0.json"
    referenceNumber: ClassVar[int] = 271
    longName: ClassVar[str] = "Educational Community License v1.0"
    licenseId: ClassVar[str] = "ECL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/ECL-1.0']
    isOsiApproved: ClassVar[bool] = True

class LicenseEcl2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/ECL-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/ECL-2.0.json"
    referenceNumber: ClassVar[int] = 260
    longName: ClassVar[str] = "Educational Community License v2.0"
    licenseId: ClassVar[str] = "ECL-2.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/ECL-2.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseEcos2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/eCos-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/eCos-2.0.json"
    referenceNumber: ClassVar[int] = 486
    longName: ClassVar[str] = "eCos license version 2.0"
    licenseId: ClassVar[str] = "eCos-2.0"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/ecos-license.html']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseEfl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/EFL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/EFL-1.0.json"
    referenceNumber: ClassVar[int] = 292
    longName: ClassVar[str] = "Eiffel Forum License v1.0"
    licenseId: ClassVar[str] = "EFL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://www.eiffel-nice.org/license/forum.txt', 'https://opensource.org/licenses/EFL-1.0']
    isOsiApproved: ClassVar[bool] = True

class LicenseEfl2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/EFL-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/EFL-2.0.json"
    referenceNumber: ClassVar[int] = 129
    longName: ClassVar[str] = "Eiffel Forum License v2.0"
    licenseId: ClassVar[str] = "EFL-2.0"
    seeAlso: ClassVar[List[str]] = ['http://www.eiffel-nice.org/license/eiffel-forum-license-2.html', 'https://opensource.org/licenses/EFL-2.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseEgenix(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/eGenix.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/eGenix.json"
    referenceNumber: ClassVar[int] = 48
    longName: ClassVar[str] = "eGenix.com Public License 1.1.0"
    licenseId: ClassVar[str] = "eGenix"
    seeAlso: ClassVar[List[str]] = ['http://www.egenix.com/products/eGenix.com-Public-License-1.1.0.pdf', 'https://fedoraproject.org/wiki/Licensing/eGenix.com_Public_License_1.1.0']
    isOsiApproved: ClassVar[bool] = False

class LicenseElastic2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Elastic-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Elastic-2.0.json"
    referenceNumber: ClassVar[int] = 377
    longName: ClassVar[str] = "Elastic License 2.0"
    licenseId: ClassVar[str] = "Elastic-2.0"
    seeAlso: ClassVar[List[str]] = ['https://www.elastic.co/licensing/elastic-license', 'https://github.com/elastic/elasticsearch/blob/master/licenses/ELASTIC-LICENSE-2.0.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseEntessa(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Entessa.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Entessa.json"
    referenceNumber: ClassVar[int] = 210
    longName: ClassVar[str] = "Entessa Public License v1.0"
    licenseId: ClassVar[str] = "Entessa"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/Entessa']
    isOsiApproved: ClassVar[bool] = True

class LicenseEpics(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/EPICS.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/EPICS.json"
    referenceNumber: ClassVar[int] = 532
    longName: ClassVar[str] = "EPICS Open License"
    licenseId: ClassVar[str] = "EPICS"
    seeAlso: ClassVar[List[str]] = ['https://epics.anl.gov/license/open.php']
    isOsiApproved: ClassVar[bool] = False

class LicenseEpl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/EPL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/EPL-1.0.json"
    referenceNumber: ClassVar[int] = 145
    longName: ClassVar[str] = "Eclipse Public License 1.0"
    licenseId: ClassVar[str] = "EPL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://www.eclipse.org/legal/epl-v10.html', 'https://opensource.org/licenses/EPL-1.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseEpl2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/EPL-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/EPL-2.0.json"
    referenceNumber: ClassVar[int] = 441
    longName: ClassVar[str] = "Eclipse Public License 2.0"
    licenseId: ClassVar[str] = "EPL-2.0"
    seeAlso: ClassVar[List[str]] = ['https://www.eclipse.org/legal/epl-2.0', 'https://www.opensource.org/licenses/EPL-2.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseErlpl1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/ErlPL-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/ErlPL-1.1.json"
    referenceNumber: ClassVar[int] = 258
    longName: ClassVar[str] = "Erlang Public License v1.1"
    licenseId: ClassVar[str] = "ErlPL-1.1"
    seeAlso: ClassVar[List[str]] = ['http://www.erlang.org/EPLICENSE']
    isOsiApproved: ClassVar[bool] = False

class LicenseEtalab2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/etalab-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/etalab-2.0.json"
    referenceNumber: ClassVar[int] = 379
    longName: ClassVar[str] = "Etalab Open License 2.0"
    licenseId: ClassVar[str] = "etalab-2.0"
    seeAlso: ClassVar[List[str]] = ['https://github.com/DISIC/politique-de-contribution-open-source/blob/master/LICENSE.pdf', 'https://raw.githubusercontent.com/DISIC/politique-de-contribution-open-source/master/LICENSE']
    isOsiApproved: ClassVar[bool] = False

class LicenseEudatagrid(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/EUDatagrid.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/EUDatagrid.json"
    referenceNumber: ClassVar[int] = 1
    longName: ClassVar[str] = "EU DataGrid Software License"
    licenseId: ClassVar[str] = "EUDatagrid"
    seeAlso: ClassVar[List[str]] = ['http://eu-datagrid.web.cern.ch/eu-datagrid/license.html', 'https://opensource.org/licenses/EUDatagrid']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseEupl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/EUPL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/EUPL-1.0.json"
    referenceNumber: ClassVar[int] = 101
    longName: ClassVar[str] = "European Union Public License 1.0"
    licenseId: ClassVar[str] = "EUPL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://ec.europa.eu/idabc/en/document/7330.html', 'http://ec.europa.eu/idabc/servlets/Doc027f.pdf?id=31096']
    isOsiApproved: ClassVar[bool] = False

class LicenseEupl1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/EUPL-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/EUPL-1.1.json"
    referenceNumber: ClassVar[int] = 584
    longName: ClassVar[str] = "European Union Public License 1.1"
    licenseId: ClassVar[str] = "EUPL-1.1"
    seeAlso: ClassVar[List[str]] = ['https://joinup.ec.europa.eu/software/page/eupl/licence-eupl', 'https://joinup.ec.europa.eu/sites/default/files/custom-page/attachment/eupl1.1.-licence-en_0.pdf', 'https://opensource.org/licenses/EUPL-1.1']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseEupl1_2(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/EUPL-1.2.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/EUPL-1.2.json"
    referenceNumber: ClassVar[int] = 69
    longName: ClassVar[str] = "European Union Public License 1.2"
    licenseId: ClassVar[str] = "EUPL-1.2"
    seeAlso: ClassVar[List[str]] = ['https://joinup.ec.europa.eu/page/eupl-text-11-12', 'https://joinup.ec.europa.eu/sites/default/files/custom-page/attachment/eupl_v1.2_en.pdf', 'https://joinup.ec.europa.eu/sites/default/files/custom-page/attachment/2020-03/EUPL-1.2%20EN.txt', 'https://joinup.ec.europa.eu/sites/default/files/inline-files/EUPL%20v1_2%20EN(1).txt', 'http://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32017D0863', 'https://opensource.org/licenses/EUPL-1.2']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseEurosym(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Eurosym.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Eurosym.json"
    referenceNumber: ClassVar[int] = 173
    longName: ClassVar[str] = "Eurosym License"
    licenseId: ClassVar[str] = "Eurosym"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Eurosym']
    isOsiApproved: ClassVar[bool] = False

class LicenseFair(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Fair.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Fair.json"
    referenceNumber: ClassVar[int] = 307
    longName: ClassVar[str] = "Fair License"
    licenseId: ClassVar[str] = "Fair"
    seeAlso: ClassVar[List[str]] = ['http://fairlicense.org/', 'https://opensource.org/licenses/Fair']
    isOsiApproved: ClassVar[bool] = True

class LicenseFbm(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/FBM.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/FBM.json"
    referenceNumber: ClassVar[int] = 431
    longName: ClassVar[str] = "Fuzzy Bitmap License"
    licenseId: ClassVar[str] = "FBM"
    seeAlso: ClassVar[List[str]] = ['https://github.com/SWI-Prolog/packages-xpce/blob/161a40cd82004f731ba48024f9d30af388a7edf5/src/img/gifwrite.c#L21-L26']
    isOsiApproved: ClassVar[bool] = False

class LicenseFdkAac(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/FDK-AAC.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/FDK-AAC.json"
    referenceNumber: ClassVar[int] = 305
    longName: ClassVar[str] = "Fraunhofer FDK AAC Codec Library"
    licenseId: ClassVar[str] = "FDK-AAC"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/FDK-AAC', 'https://directory.fsf.org/wiki/License:Fdk']
    isOsiApproved: ClassVar[bool] = False

class LicenseFergusonTwofish(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Ferguson-Twofish.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Ferguson-Twofish.json"
    referenceNumber: ClassVar[int] = 590
    longName: ClassVar[str] = "Ferguson Twofish License"
    licenseId: ClassVar[str] = "Ferguson-Twofish"
    seeAlso: ClassVar[List[str]] = ['https://github.com/wernerd/ZRTPCPP/blob/6b3cd8e6783642292bad0c21e3e5e5ce45ff3e03/cryptcommon/twofish.c#L113C3-L127']
    isOsiApproved: ClassVar[bool] = False

class LicenseFrameworx1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Frameworx-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Frameworx-1.0.json"
    referenceNumber: ClassVar[int] = 449
    longName: ClassVar[str] = "Frameworx Open License 1.0"
    licenseId: ClassVar[str] = "Frameworx-1.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/Frameworx-1.0']
    isOsiApproved: ClassVar[bool] = True

class LicenseFreebsdDoc(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/FreeBSD-DOC.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/FreeBSD-DOC.json"
    referenceNumber: ClassVar[int] = 561
    longName: ClassVar[str] = "FreeBSD Documentation License"
    licenseId: ClassVar[str] = "FreeBSD-DOC"
    seeAlso: ClassVar[List[str]] = ['https://www.freebsd.org/copyright/freebsd-doc-license/']
    isOsiApproved: ClassVar[bool] = False

class LicenseFreeimage(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/FreeImage.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/FreeImage.json"
    referenceNumber: ClassVar[int] = 312
    longName: ClassVar[str] = "FreeImage Public License v1.0"
    licenseId: ClassVar[str] = "FreeImage"
    seeAlso: ClassVar[List[str]] = ['http://freeimage.sourceforge.net/freeimage-license.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseFsfap(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/FSFAP.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/FSFAP.json"
    referenceNumber: ClassVar[int] = 404
    longName: ClassVar[str] = "FSF All Permissive License"
    licenseId: ClassVar[str] = "FSFAP"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/prep/maintain/html_node/License-Notices-for-Other-Files.html']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseFsful(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/FSFUL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/FSFUL.json"
    referenceNumber: ClassVar[int] = 36
    longName: ClassVar[str] = "FSF Unlimited License"
    licenseId: ClassVar[str] = "FSFUL"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/FSF_Unlimited_License']
    isOsiApproved: ClassVar[bool] = False

class LicenseFsfullr(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/FSFULLR.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/FSFULLR.json"
    referenceNumber: ClassVar[int] = 434
    longName: ClassVar[str] = "FSF Unlimited License (with License Retention)"
    licenseId: ClassVar[str] = "FSFULLR"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/FSF_Unlimited_License#License_Retention_Variant']
    isOsiApproved: ClassVar[bool] = False

class LicenseFsfullrwd(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/FSFULLRWD.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/FSFULLRWD.json"
    referenceNumber: ClassVar[int] = 18
    longName: ClassVar[str] = "FSF Unlimited License (With License Retention and Warranty Disclaimer)"
    licenseId: ClassVar[str] = "FSFULLRWD"
    seeAlso: ClassVar[List[str]] = ['https://lists.gnu.org/archive/html/autoconf/2012-04/msg00061.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseFtl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/FTL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/FTL.json"
    referenceNumber: ClassVar[int] = 234
    longName: ClassVar[str] = "Freetype Project License"
    licenseId: ClassVar[str] = "FTL"
    seeAlso: ClassVar[List[str]] = ['http://freetype.fis.uniroma2.it/FTL.TXT', 'http://git.savannah.gnu.org/cgit/freetype/freetype2.git/tree/docs/FTL.TXT', 'http://gitlab.freedesktop.org/freetype/freetype/-/raw/master/docs/FTL.TXT']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseFuruseth(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Furuseth.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Furuseth.json"
    referenceNumber: ClassVar[int] = 278
    longName: ClassVar[str] = "Furuseth License"
    licenseId: ClassVar[str] = "Furuseth"
    seeAlso: ClassVar[List[str]] = ['https://git.openldap.org/openldap/openldap/-/blob/master/COPYRIGHT?ref_type=heads#L39-51']
    isOsiApproved: ClassVar[bool] = False

class LicenseFwlw(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/fwlw.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/fwlw.json"
    referenceNumber: ClassVar[int] = 168
    longName: ClassVar[str] = "fwlw License"
    licenseId: ClassVar[str] = "fwlw"
    seeAlso: ClassVar[List[str]] = ['https://mirrors.nic.cz/tex-archive/macros/latex/contrib/fwlw/README']
    isOsiApproved: ClassVar[bool] = False

class LicenseGcrDocs(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GCR-docs.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GCR-docs.json"
    referenceNumber: ClassVar[int] = 112
    longName: ClassVar[str] = "Gnome GCR Documentation License"
    licenseId: ClassVar[str] = "GCR-docs"
    seeAlso: ClassVar[List[str]] = ['https://github.com/GNOME/gcr/blob/master/docs/COPYING']
    isOsiApproved: ClassVar[bool] = False

class LicenseGd(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GD.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GD.json"
    referenceNumber: ClassVar[int] = 494
    longName: ClassVar[str] = "GD License"
    licenseId: ClassVar[str] = "GD"
    seeAlso: ClassVar[List[str]] = ['https://libgd.github.io/manuals/2.3.0/files/license-txt.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseGfdl1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.1.json"
    referenceNumber: ClassVar[int] = 164
    longName: ClassVar[str] = "GNU Free Documentation License v1.1"
    licenseId: ClassVar[str] = "GFDL-1.1"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseGfdl1_1InvariantsOnly(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.1-invariants-only.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.1-invariants-only.json"
    referenceNumber: ClassVar[int] = 373
    longName: ClassVar[str] = "GNU Free Documentation License v1.1 only - invariants"
    licenseId: ClassVar[str] = "GFDL-1.1-invariants-only"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseGfdl1_1InvariantsOrLater(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.1-invariants-or-later.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.1-invariants-or-later.json"
    referenceNumber: ClassVar[int] = 38
    longName: ClassVar[str] = "GNU Free Documentation License v1.1 or later - invariants"
    licenseId: ClassVar[str] = "GFDL-1.1-invariants-or-later"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseGfdl1_1NoInvariantsOnly(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.1-no-invariants-only.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.1-no-invariants-only.json"
    referenceNumber: ClassVar[int] = 355
    longName: ClassVar[str] = "GNU Free Documentation License v1.1 only - no invariants"
    licenseId: ClassVar[str] = "GFDL-1.1-no-invariants-only"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseGfdl1_1NoInvariantsOrLater(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.1-no-invariants-or-later.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.1-no-invariants-or-later.json"
    referenceNumber: ClassVar[int] = 340
    longName: ClassVar[str] = "GNU Free Documentation License v1.1 or later - no invariants"
    licenseId: ClassVar[str] = "GFDL-1.1-no-invariants-or-later"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseGfdl1_1Only(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.1-only.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.1-only.json"
    referenceNumber: ClassVar[int] = 59
    longName: ClassVar[str] = "GNU Free Documentation License v1.1 only"
    licenseId: ClassVar[str] = "GFDL-1.1-only"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseGfdl1_1OrLater(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.1-or-later.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.1-or-later.json"
    referenceNumber: ClassVar[int] = 563
    longName: ClassVar[str] = "GNU Free Documentation License v1.1 or later"
    licenseId: ClassVar[str] = "GFDL-1.1-or-later"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/fdl-1.1.txt']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseGfdl1_2(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.2.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.2.json"
    referenceNumber: ClassVar[int] = 544
    longName: ClassVar[str] = "GNU Free Documentation License v1.2"
    licenseId: ClassVar[str] = "GFDL-1.2"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseGfdl1_2InvariantsOnly(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.2-invariants-only.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.2-invariants-only.json"
    referenceNumber: ClassVar[int] = 9
    longName: ClassVar[str] = "GNU Free Documentation License v1.2 only - invariants"
    licenseId: ClassVar[str] = "GFDL-1.2-invariants-only"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseGfdl1_2InvariantsOrLater(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.2-invariants-or-later.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.2-invariants-or-later.json"
    referenceNumber: ClassVar[int] = 30
    longName: ClassVar[str] = "GNU Free Documentation License v1.2 or later - invariants"
    licenseId: ClassVar[str] = "GFDL-1.2-invariants-or-later"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseGfdl1_2NoInvariantsOnly(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.2-no-invariants-only.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.2-no-invariants-only.json"
    referenceNumber: ClassVar[int] = 496
    longName: ClassVar[str] = "GNU Free Documentation License v1.2 only - no invariants"
    licenseId: ClassVar[str] = "GFDL-1.2-no-invariants-only"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseGfdl1_2NoInvariantsOrLater(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.2-no-invariants-or-later.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.2-no-invariants-or-later.json"
    referenceNumber: ClassVar[int] = 122
    longName: ClassVar[str] = "GNU Free Documentation License v1.2 or later - no invariants"
    licenseId: ClassVar[str] = "GFDL-1.2-no-invariants-or-later"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseGfdl1_2Only(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.2-only.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.2-only.json"
    referenceNumber: ClassVar[int] = 523
    longName: ClassVar[str] = "GNU Free Documentation License v1.2 only"
    licenseId: ClassVar[str] = "GFDL-1.2-only"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseGfdl1_2OrLater(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.2-or-later.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.2-or-later.json"
    referenceNumber: ClassVar[int] = 187
    longName: ClassVar[str] = "GNU Free Documentation License v1.2 or later"
    licenseId: ClassVar[str] = "GFDL-1.2-or-later"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/fdl-1.2.txt']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseGfdl1_3(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.3.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.3.json"
    referenceNumber: ClassVar[int] = 598
    longName: ClassVar[str] = "GNU Free Documentation License v1.3"
    licenseId: ClassVar[str] = "GFDL-1.3"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/fdl-1.3.txt']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseGfdl1_3InvariantsOnly(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.3-invariants-only.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.3-invariants-only.json"
    referenceNumber: ClassVar[int] = 353
    longName: ClassVar[str] = "GNU Free Documentation License v1.3 only - invariants"
    licenseId: ClassVar[str] = "GFDL-1.3-invariants-only"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/fdl-1.3.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseGfdl1_3InvariantsOrLater(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.3-invariants-or-later.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.3-invariants-or-later.json"
    referenceNumber: ClassVar[int] = 344
    longName: ClassVar[str] = "GNU Free Documentation License v1.3 or later - invariants"
    licenseId: ClassVar[str] = "GFDL-1.3-invariants-or-later"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/fdl-1.3.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseGfdl1_3NoInvariantsOnly(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.3-no-invariants-only.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.3-no-invariants-only.json"
    referenceNumber: ClassVar[int] = 479
    longName: ClassVar[str] = "GNU Free Documentation License v1.3 only - no invariants"
    licenseId: ClassVar[str] = "GFDL-1.3-no-invariants-only"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/fdl-1.3.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseGfdl1_3NoInvariantsOrLater(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.3-no-invariants-or-later.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.3-no-invariants-or-later.json"
    referenceNumber: ClassVar[int] = 516
    longName: ClassVar[str] = "GNU Free Documentation License v1.3 or later - no invariants"
    licenseId: ClassVar[str] = "GFDL-1.3-no-invariants-or-later"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/fdl-1.3.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseGfdl1_3Only(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.3-only.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.3-only.json"
    referenceNumber: ClassVar[int] = 115
    longName: ClassVar[str] = "GNU Free Documentation License v1.3 only"
    licenseId: ClassVar[str] = "GFDL-1.3-only"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/fdl-1.3.txt']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseGfdl1_3OrLater(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.3-or-later.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GFDL-1.3-or-later.json"
    referenceNumber: ClassVar[int] = 440
    longName: ClassVar[str] = "GNU Free Documentation License v1.3 or later"
    licenseId: ClassVar[str] = "GFDL-1.3-or-later"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/fdl-1.3.txt']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseGiftware(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Giftware.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Giftware.json"
    referenceNumber: ClassVar[int] = 13
    longName: ClassVar[str] = "Giftware License"
    licenseId: ClassVar[str] = "Giftware"
    seeAlso: ClassVar[List[str]] = ['http://liballeg.org/license.html#allegro-4-the-giftware-license']
    isOsiApproved: ClassVar[bool] = False

class LicenseGl2ps(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GL2PS.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GL2PS.json"
    referenceNumber: ClassVar[int] = 254
    longName: ClassVar[str] = "GL2PS License"
    licenseId: ClassVar[str] = "GL2PS"
    seeAlso: ClassVar[List[str]] = ['http://www.geuz.org/gl2ps/COPYING.GL2PS']
    isOsiApproved: ClassVar[bool] = False

class LicenseGlide(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Glide.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Glide.json"
    referenceNumber: ClassVar[int] = 206
    longName: ClassVar[str] = "3dfx Glide License"
    licenseId: ClassVar[str] = "Glide"
    seeAlso: ClassVar[List[str]] = ['http://www.users.on.net/~triforce/glidexp/COPYING.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseGlulxe(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Glulxe.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Glulxe.json"
    referenceNumber: ClassVar[int] = 405
    longName: ClassVar[str] = "Glulxe License"
    licenseId: ClassVar[str] = "Glulxe"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Glulxe']
    isOsiApproved: ClassVar[bool] = False

class LicenseGlwtpl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GLWTPL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GLWTPL.json"
    referenceNumber: ClassVar[int] = 268
    longName: ClassVar[str] = "Good Luck With That Public License"
    licenseId: ClassVar[str] = "GLWTPL"
    seeAlso: ClassVar[List[str]] = ['https://github.com/me-shaon/GLWTPL/commit/da5f6bc734095efbacb442c0b31e33a65b9d6e85']
    isOsiApproved: ClassVar[bool] = False

class LicenseGnuplot(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/gnuplot.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/gnuplot.json"
    referenceNumber: ClassVar[int] = 178
    longName: ClassVar[str] = "gnuplot License"
    licenseId: ClassVar[str] = "gnuplot"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Gnuplot']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseGpl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GPL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GPL-1.0.json"
    referenceNumber: ClassVar[int] = 257
    longName: ClassVar[str] = "GNU General Public License v1.0 only"
    licenseId: ClassVar[str] = "GPL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/gpl-1.0-standalone.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseGpl1_0Plus(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GPL-1.0+.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GPL-1.0+.json"
    referenceNumber: ClassVar[int] = 459
    longName: ClassVar[str] = "GNU General Public License v1.0 or later"
    licenseId: ClassVar[str] = "GPL-1.0+"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/gpl-1.0-standalone.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseGpl1_0Only(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GPL-1.0-only.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GPL-1.0-only.json"
    referenceNumber: ClassVar[int] = 454
    longName: ClassVar[str] = "GNU General Public License v1.0 only"
    licenseId: ClassVar[str] = "GPL-1.0-only"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/gpl-1.0-standalone.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseGpl1_0OrLater(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GPL-1.0-or-later.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GPL-1.0-or-later.json"
    referenceNumber: ClassVar[int] = 365
    longName: ClassVar[str] = "GNU General Public License v1.0 or later"
    licenseId: ClassVar[str] = "GPL-1.0-or-later"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/gpl-1.0-standalone.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseGpl2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GPL-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GPL-2.0.json"
    referenceNumber: ClassVar[int] = 548
    longName: ClassVar[str] = "GNU General Public License v2.0 only"
    licenseId: ClassVar[str] = "GPL-2.0"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html', 'https://opensource.org/licenses/GPL-2.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseGpl2_0Plus(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GPL-2.0+.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GPL-2.0+.json"
    referenceNumber: ClassVar[int] = 108
    longName: ClassVar[str] = "GNU General Public License v2.0 or later"
    licenseId: ClassVar[str] = "GPL-2.0+"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html', 'https://opensource.org/licenses/GPL-2.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseGpl2_0Only(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GPL-2.0-only.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GPL-2.0-only.json"
    referenceNumber: ClassVar[int] = 171
    longName: ClassVar[str] = "GNU General Public License v2.0 only"
    licenseId: ClassVar[str] = "GPL-2.0-only"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html', 'https://opensource.org/licenses/GPL-2.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseGpl2_0OrLater(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GPL-2.0-or-later.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GPL-2.0-or-later.json"
    referenceNumber: ClassVar[int] = 464
    longName: ClassVar[str] = "GNU General Public License v2.0 or later"
    licenseId: ClassVar[str] = "GPL-2.0-or-later"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html', 'https://opensource.org/licenses/GPL-2.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseGpl2_0WithAutoconfException(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GPL-2.0-with-autoconf-exception.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GPL-2.0-with-autoconf-exception.json"
    referenceNumber: ClassVar[int] = 251
    longName: ClassVar[str] = "GNU General Public License v2.0 w/Autoconf exception"
    licenseId: ClassVar[str] = "GPL-2.0-with-autoconf-exception"
    seeAlso: ClassVar[List[str]] = ['http://ac-archive.sourceforge.net/doc/copyright.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseGpl2_0WithBisonException(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GPL-2.0-with-bison-exception.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GPL-2.0-with-bison-exception.json"
    referenceNumber: ClassVar[int] = 77
    longName: ClassVar[str] = "GNU General Public License v2.0 w/Bison exception"
    licenseId: ClassVar[str] = "GPL-2.0-with-bison-exception"
    seeAlso: ClassVar[List[str]] = ['http://git.savannah.gnu.org/cgit/bison.git/tree/data/yacc.c?id=193d7c7054ba7197b0789e14965b739162319b5e#n141']
    isOsiApproved: ClassVar[bool] = False

class LicenseGpl2_0WithClasspathException(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GPL-2.0-with-classpath-exception.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GPL-2.0-with-classpath-exception.json"
    referenceNumber: ClassVar[int] = 519
    longName: ClassVar[str] = "GNU General Public License v2.0 w/Classpath exception"
    licenseId: ClassVar[str] = "GPL-2.0-with-classpath-exception"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/software/classpath/license.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseGpl2_0WithFontException(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GPL-2.0-with-font-exception.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GPL-2.0-with-font-exception.json"
    referenceNumber: ClassVar[int] = 161
    longName: ClassVar[str] = "GNU General Public License v2.0 w/Font exception"
    licenseId: ClassVar[str] = "GPL-2.0-with-font-exception"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/gpl-faq.html#FontException']
    isOsiApproved: ClassVar[bool] = False

class LicenseGpl2_0WithGccException(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GPL-2.0-with-GCC-exception.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GPL-2.0-with-GCC-exception.json"
    referenceNumber: ClassVar[int] = 401
    longName: ClassVar[str] = "GNU General Public License v2.0 w/GCC Runtime Library exception"
    licenseId: ClassVar[str] = "GPL-2.0-with-GCC-exception"
    seeAlso: ClassVar[List[str]] = ['https://gcc.gnu.org/git/?p=gcc.git;a=blob;f=gcc/libgcc1.c;h=762f5143fc6eed57b6797c82710f3538aa52b40b;hb=cb143a3ce4fb417c68f5fa2691a1b1b1053dfba9#l10']
    isOsiApproved: ClassVar[bool] = False

class LicenseGpl3_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GPL-3.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GPL-3.0.json"
    referenceNumber: ClassVar[int] = 29
    longName: ClassVar[str] = "GNU General Public License v3.0 only"
    licenseId: ClassVar[str] = "GPL-3.0"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/gpl-3.0-standalone.html', 'https://opensource.org/licenses/GPL-3.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseGpl3_0Plus(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GPL-3.0+.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GPL-3.0+.json"
    referenceNumber: ClassVar[int] = 557
    longName: ClassVar[str] = "GNU General Public License v3.0 or later"
    licenseId: ClassVar[str] = "GPL-3.0+"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/gpl-3.0-standalone.html', 'https://opensource.org/licenses/GPL-3.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseGpl3_0Only(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GPL-3.0-only.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GPL-3.0-only.json"
    referenceNumber: ClassVar[int] = 190
    longName: ClassVar[str] = "GNU General Public License v3.0 only"
    licenseId: ClassVar[str] = "GPL-3.0-only"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/gpl-3.0-standalone.html', 'https://opensource.org/licenses/GPL-3.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseGpl3_0OrLater(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GPL-3.0-or-later.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GPL-3.0-or-later.json"
    referenceNumber: ClassVar[int] = 543
    longName: ClassVar[str] = "GNU General Public License v3.0 or later"
    licenseId: ClassVar[str] = "GPL-3.0-or-later"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/gpl-3.0-standalone.html', 'https://opensource.org/licenses/GPL-3.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseGpl3_0WithAutoconfException(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GPL-3.0-with-autoconf-exception.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GPL-3.0-with-autoconf-exception.json"
    referenceNumber: ClassVar[int] = 417
    longName: ClassVar[str] = "GNU General Public License v3.0 w/Autoconf exception"
    licenseId: ClassVar[str] = "GPL-3.0-with-autoconf-exception"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/autoconf-exception-3.0.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseGpl3_0WithGccException(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/GPL-3.0-with-GCC-exception.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/GPL-3.0-with-GCC-exception.json"
    referenceNumber: ClassVar[int] = 302
    longName: ClassVar[str] = "GNU General Public License v3.0 w/GCC Runtime Library exception"
    licenseId: ClassVar[str] = "GPL-3.0-with-GCC-exception"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/gcc-exception-3.1.html']
    isOsiApproved: ClassVar[bool] = True

class LicenseGraphicsGems(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Graphics-Gems.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Graphics-Gems.json"
    referenceNumber: ClassVar[int] = 232
    longName: ClassVar[str] = "Graphics Gems License"
    licenseId: ClassVar[str] = "Graphics-Gems"
    seeAlso: ClassVar[List[str]] = ['https://github.com/erich666/GraphicsGems/blob/master/LICENSE.md']
    isOsiApproved: ClassVar[bool] = False

class LicenseGsoap1_3b(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/gSOAP-1.3b.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/gSOAP-1.3b.json"
    referenceNumber: ClassVar[int] = 429
    longName: ClassVar[str] = "gSOAP Public License v1.3b"
    licenseId: ClassVar[str] = "gSOAP-1.3b"
    seeAlso: ClassVar[List[str]] = ['http://www.cs.fsu.edu/~engelen/license.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseHaskellreport(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/HaskellReport.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/HaskellReport.json"
    referenceNumber: ClassVar[int] = 485
    longName: ClassVar[str] = "Haskell Language Report License"
    licenseId: ClassVar[str] = "HaskellReport"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Haskell_Language_Report_License']
    isOsiApproved: ClassVar[bool] = False

class LicenseHdparm(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/hdparm.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/hdparm.json"
    referenceNumber: ClassVar[int] = 126
    longName: ClassVar[str] = "hdparm License"
    licenseId: ClassVar[str] = "hdparm"
    seeAlso: ClassVar[List[str]] = ['https://github.com/Distrotech/hdparm/blob/4517550db29a91420fb2b020349523b1b4512df2/LICENSE.TXT']
    isOsiApproved: ClassVar[bool] = False

class LicenseHippocratic2_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Hippocratic-2.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Hippocratic-2.1.json"
    referenceNumber: ClassVar[int] = 200
    longName: ClassVar[str] = "Hippocratic License 2.1"
    licenseId: ClassVar[str] = "Hippocratic-2.1"
    seeAlso: ClassVar[List[str]] = ['https://firstdonoharm.dev/version/2/1/license.html', 'https://github.com/EthicalSource/hippocratic-license/blob/58c0e646d64ff6fbee275bfe2b9492f914e3ab2a/LICENSE.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseHp1986(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/HP-1986.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/HP-1986.json"
    referenceNumber: ClassVar[int] = 81
    longName: ClassVar[str] = "Hewlett-Packard 1986 License"
    licenseId: ClassVar[str] = "HP-1986"
    seeAlso: ClassVar[List[str]] = ['https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/machine/hppa/memchr.S;h=1cca3e5e8867aa4bffef1f75a5c1bba25c0c441e;hb=HEAD#l2']
    isOsiApproved: ClassVar[bool] = False

class LicenseHp1989(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/HP-1989.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/HP-1989.json"
    referenceNumber: ClassVar[int] = 412
    longName: ClassVar[str] = "Hewlett-Packard 1989 License"
    licenseId: ClassVar[str] = "HP-1989"
    seeAlso: ClassVar[List[str]] = ['https://github.com/bleargh45/Data-UUID/blob/master/LICENSE']
    isOsiApproved: ClassVar[bool] = False

class LicenseHpnd(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/HPND.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/HPND.json"
    referenceNumber: ClassVar[int] = 5
    longName: ClassVar[str] = "Historical Permission Notice and Disclaimer"
    licenseId: ClassVar[str] = "HPND"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/HPND', 'http://lists.opensource.org/pipermail/license-discuss_lists.opensource.org/2002-November/006304.html']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseHpndDec(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/HPND-DEC.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/HPND-DEC.json"
    referenceNumber: ClassVar[int] = 413
    longName: ClassVar[str] = "Historical Permission Notice and Disclaimer - DEC variant"
    licenseId: ClassVar[str] = "HPND-DEC"
    seeAlso: ClassVar[List[str]] = ['https://gitlab.freedesktop.org/xorg/app/xkbcomp/-/blob/master/COPYING?ref_type=heads#L69']
    isOsiApproved: ClassVar[bool] = False

class LicenseHpndDoc(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/HPND-doc.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/HPND-doc.json"
    referenceNumber: ClassVar[int] = 95
    longName: ClassVar[str] = "Historical Permission Notice and Disclaimer - documentation variant"
    licenseId: ClassVar[str] = "HPND-doc"
    seeAlso: ClassVar[List[str]] = ['https://gitlab.freedesktop.org/xorg/lib/libxext/-/blob/master/COPYING?ref_type=heads#L185-197', 'https://gitlab.freedesktop.org/xorg/lib/libxtst/-/blob/master/COPYING?ref_type=heads#L70-77']
    isOsiApproved: ClassVar[bool] = False

class LicenseHpndDocSell(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/HPND-doc-sell.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/HPND-doc-sell.json"
    referenceNumber: ClassVar[int] = 542
    longName: ClassVar[str] = "Historical Permission Notice and Disclaimer - documentation sell variant"
    licenseId: ClassVar[str] = "HPND-doc-sell"
    seeAlso: ClassVar[List[str]] = ['https://gitlab.freedesktop.org/xorg/lib/libxtst/-/blob/master/COPYING?ref_type=heads#L108-117', 'https://gitlab.freedesktop.org/xorg/lib/libxext/-/blob/master/COPYING?ref_type=heads#L153-162']
    isOsiApproved: ClassVar[bool] = False

class LicenseHpndExportUs(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/HPND-export-US.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/HPND-export-US.json"
    referenceNumber: ClassVar[int] = 217
    longName: ClassVar[str] = "HPND with US Government export control warning"
    licenseId: ClassVar[str] = "HPND-export-US"
    seeAlso: ClassVar[List[str]] = ['https://www.kermitproject.org/ck90.html#source']
    isOsiApproved: ClassVar[bool] = False

class LicenseHpndExportUsModify(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/HPND-export-US-modify.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/HPND-export-US-modify.json"
    referenceNumber: ClassVar[int] = 372
    longName: ClassVar[str] = "HPND with US Government export control warning and modification rqmt"
    licenseId: ClassVar[str] = "HPND-export-US-modify"
    seeAlso: ClassVar[List[str]] = ['https://github.com/krb5/krb5/blob/krb5-1.21.2-final/NOTICE#L1157-L1182', 'https://github.com/pythongssapi/k5test/blob/v0.10.3/K5TEST-LICENSE.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseHpndMarkusKuhn(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/HPND-Markus-Kuhn.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/HPND-Markus-Kuhn.json"
    referenceNumber: ClassVar[int] = 436
    longName: ClassVar[str] = "Historical Permission Notice and Disclaimer - Markus Kuhn variant"
    licenseId: ClassVar[str] = "HPND-Markus-Kuhn"
    seeAlso: ClassVar[List[str]] = ['https://www.cl.cam.ac.uk/~mgk25/ucs/wcwidth.c', 'https://sourceware.org/git/?p=binutils-gdb.git;a=blob;f=readline/readline/support/wcwidth.c;h=0f5ec995796f4813abbcf4972aec0378ab74722a;hb=HEAD#l55']
    isOsiApproved: ClassVar[bool] = False

class LicenseHpndPbmplus(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/HPND-Pbmplus.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/HPND-Pbmplus.json"
    referenceNumber: ClassVar[int] = 474
    longName: ClassVar[str] = "Historical Permission Notice and Disclaimer - Pbmplus variant"
    licenseId: ClassVar[str] = "HPND-Pbmplus"
    seeAlso: ClassVar[List[str]] = ['https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/netpbm.c#l8']
    isOsiApproved: ClassVar[bool] = False

class LicenseHpndSellMitDisclaimerXserver(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/HPND-sell-MIT-disclaimer-xserver.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/HPND-sell-MIT-disclaimer-xserver.json"
    referenceNumber: ClassVar[int] = 202
    longName: ClassVar[str] = "Historical Permission Notice and Disclaimer - sell xserver variant with MIT disclaimer"
    licenseId: ClassVar[str] = "HPND-sell-MIT-disclaimer-xserver"
    seeAlso: ClassVar[List[str]] = ['https://gitlab.freedesktop.org/xorg/xserver/-/blob/master/COPYING?ref_type=heads#L1781']
    isOsiApproved: ClassVar[bool] = False

class LicenseHpndSellRegexpr(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/HPND-sell-regexpr.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/HPND-sell-regexpr.json"
    referenceNumber: ClassVar[int] = 549
    longName: ClassVar[str] = "Historical Permission Notice and Disclaimer - sell regexpr variant"
    licenseId: ClassVar[str] = "HPND-sell-regexpr"
    seeAlso: ClassVar[List[str]] = ['https://gitlab.com/bacula-org/bacula/-/blob/Branch-11.0/bacula/LICENSE-FOSS?ref_type=heads#L245']
    isOsiApproved: ClassVar[bool] = False

class LicenseHpndSellVariant(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/HPND-sell-variant.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/HPND-sell-variant.json"
    referenceNumber: ClassVar[int] = 21
    longName: ClassVar[str] = "Historical Permission Notice and Disclaimer - sell variant"
    licenseId: ClassVar[str] = "HPND-sell-variant"
    seeAlso: ClassVar[List[str]] = ['https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/net/sunrpc/auth_gss/gss_generic_token.c?h=v4.19']
    isOsiApproved: ClassVar[bool] = False

class LicenseHpndSellVariantMitDisclaimer(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/HPND-sell-variant-MIT-disclaimer.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/HPND-sell-variant-MIT-disclaimer.json"
    referenceNumber: ClassVar[int] = 235
    longName: ClassVar[str] = "HPND sell variant with MIT disclaimer"
    licenseId: ClassVar[str] = "HPND-sell-variant-MIT-disclaimer"
    seeAlso: ClassVar[List[str]] = ['https://github.com/sigmavirus24/x11-ssh-askpass/blob/master/README']
    isOsiApproved: ClassVar[bool] = False

class LicenseHpndUc(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/HPND-UC.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/HPND-UC.json"
    referenceNumber: ClassVar[int] = 189
    longName: ClassVar[str] = "Historical Permission Notice and Disclaimer - University of California variant"
    licenseId: ClassVar[str] = "HPND-UC"
    seeAlso: ClassVar[List[str]] = ['https://core.tcl-lang.org/tk/file?name=compat/unistd.h']
    isOsiApproved: ClassVar[bool] = False

class LicenseHtmltidy(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/HTMLTIDY.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/HTMLTIDY.json"
    referenceNumber: ClassVar[int] = 358
    longName: ClassVar[str] = "HTML Tidy License"
    licenseId: ClassVar[str] = "HTMLTIDY"
    seeAlso: ClassVar[List[str]] = ['https://github.com/htacg/tidy-html5/blob/next/README/LICENSE.md']
    isOsiApproved: ClassVar[bool] = False

class LicenseIbmPibs(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/IBM-pibs.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/IBM-pibs.json"
    referenceNumber: ClassVar[int] = 367
    longName: ClassVar[str] = "IBM PowerPC Initialization and Boot Software"
    licenseId: ClassVar[str] = "IBM-pibs"
    seeAlso: ClassVar[List[str]] = ['http://git.denx.de/?p=u-boot.git;a=blob;f=arch/powerpc/cpu/ppc4xx/miiphy.c;h=297155fdafa064b955e53e9832de93bfb0cfb85b;hb=9fab4bf4cc077c21e43941866f3f2c196f28670d']
    isOsiApproved: ClassVar[bool] = False

class LicenseIcu(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/ICU.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/ICU.json"
    referenceNumber: ClassVar[int] = 495
    longName: ClassVar[str] = "ICU License"
    licenseId: ClassVar[str] = "ICU"
    seeAlso: ClassVar[List[str]] = ['http://source.icu-project.org/repos/icu/icu/trunk/license.html']
    isOsiApproved: ClassVar[bool] = True

class LicenseIecCodeComponentsEula(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/IEC-Code-Components-EULA.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/IEC-Code-Components-EULA.json"
    referenceNumber: ClassVar[int] = 41
    longName: ClassVar[str] = "IEC    Code Components End-user licence agreement"
    licenseId: ClassVar[str] = "IEC-Code-Components-EULA"
    seeAlso: ClassVar[List[str]] = ['https://www.iec.ch/webstore/custserv/pdf/CC-EULA.pdf', 'https://www.iec.ch/CCv1', 'https://www.iec.ch/copyright']
    isOsiApproved: ClassVar[bool] = False

class LicenseIjg(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/IJG.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/IJG.json"
    referenceNumber: ClassVar[int] = 396
    longName: ClassVar[str] = "Independent JPEG Group License"
    licenseId: ClassVar[str] = "IJG"
    seeAlso: ClassVar[List[str]] = ['http://dev.w3.org/cvsweb/Amaya/libjpeg/Attic/README?rev=1.2']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseIjgShort(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/IJG-short.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/IJG-short.json"
    referenceNumber: ClassVar[int] = 553
    longName: ClassVar[str] = "Independent JPEG Group License - short"
    licenseId: ClassVar[str] = "IJG-short"
    seeAlso: ClassVar[List[str]] = ['https://sourceforge.net/p/xmedcon/code/ci/master/tree/libs/ljpg/']
    isOsiApproved: ClassVar[bool] = False

class LicenseImagemagick(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/ImageMagick.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/ImageMagick.json"
    referenceNumber: ClassVar[int] = 293
    longName: ClassVar[str] = "ImageMagick License"
    licenseId: ClassVar[str] = "ImageMagick"
    seeAlso: ClassVar[List[str]] = ['http://www.imagemagick.org/script/license.php']
    isOsiApproved: ClassVar[bool] = False

class LicenseImatix(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/iMatix.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/iMatix.json"
    referenceNumber: ClassVar[int] = 409
    longName: ClassVar[str] = "iMatix Standard Function Library Agreement"
    licenseId: ClassVar[str] = "iMatix"
    seeAlso: ClassVar[List[str]] = ['http://legacy.imatix.com/html/sfl/sfl4.htm#license']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseImlib2(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Imlib2.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Imlib2.json"
    referenceNumber: ClassVar[int] = 443
    longName: ClassVar[str] = "Imlib2 License"
    licenseId: ClassVar[str] = "Imlib2"
    seeAlso: ClassVar[List[str]] = ['http://trac.enlightenment.org/e/browser/trunk/imlib2/COPYING', 'https://git.enlightenment.org/legacy/imlib2.git/tree/COPYING']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseInfoZip(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Info-ZIP.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Info-ZIP.json"
    referenceNumber: ClassVar[int] = 107
    longName: ClassVar[str] = "Info-ZIP License"
    licenseId: ClassVar[str] = "Info-ZIP"
    seeAlso: ClassVar[List[str]] = ['http://www.info-zip.org/license.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseInnerNet2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Inner-Net-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Inner-Net-2.0.json"
    referenceNumber: ClassVar[int] = 152
    longName: ClassVar[str] = "Inner Net License v2.0"
    licenseId: ClassVar[str] = "Inner-Net-2.0"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Inner_Net_License', 'https://sourceware.org/git/?p=glibc.git;a=blob;f=LICENSES;h=530893b1dc9ea00755603c68fb36bd4fc38a7be8;hb=HEAD#l207']
    isOsiApproved: ClassVar[bool] = False

class LicenseIntel(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Intel.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Intel.json"
    referenceNumber: ClassVar[int] = 132
    longName: ClassVar[str] = "Intel Open Source License"
    licenseId: ClassVar[str] = "Intel"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/Intel']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseIntelAcpi(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Intel-ACPI.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Intel-ACPI.json"
    referenceNumber: ClassVar[int] = 357
    longName: ClassVar[str] = "Intel ACPI Software License Agreement"
    licenseId: ClassVar[str] = "Intel-ACPI"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Intel_ACPI_Software_License_Agreement']
    isOsiApproved: ClassVar[bool] = False

class LicenseInterbase1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Interbase-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Interbase-1.0.json"
    referenceNumber: ClassVar[int] = 603
    longName: ClassVar[str] = "Interbase Public License v1.0"
    licenseId: ClassVar[str] = "Interbase-1.0"
    seeAlso: ClassVar[List[str]] = ['https://web.archive.org/web/20060319014854/http://info.borland.com/devsupport/interbase/opensource/IPL.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseIpa(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/IPA.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/IPA.json"
    referenceNumber: ClassVar[int] = 130
    longName: ClassVar[str] = "IPA Font License"
    licenseId: ClassVar[str] = "IPA"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/IPA']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseIpl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/IPL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/IPL-1.0.json"
    referenceNumber: ClassVar[int] = 462
    longName: ClassVar[str] = "IBM Public License v1.0"
    licenseId: ClassVar[str] = "IPL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/IPL-1.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseIsc(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/ISC.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/ISC.json"
    referenceNumber: ClassVar[int] = 40
    longName: ClassVar[str] = "ISC License"
    licenseId: ClassVar[str] = "ISC"
    seeAlso: ClassVar[List[str]] = ['https://www.isc.org/licenses/', 'https://www.isc.org/downloads/software-support-policy/isc-license/', 'https://opensource.org/licenses/ISC']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseJam(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Jam.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Jam.json"
    referenceNumber: ClassVar[int] = 389
    longName: ClassVar[str] = "Jam License"
    licenseId: ClassVar[str] = "Jam"
    seeAlso: ClassVar[List[str]] = ['https://www.boost.org/doc/libs/1_35_0/doc/html/jam.html', 'https://web.archive.org/web/20160330173339/https://swarm.workshop.perforce.com/files/guest/perforce_software/jam/src/README']
    isOsiApproved: ClassVar[bool] = True

class LicenseJasper2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/JasPer-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/JasPer-2.0.json"
    referenceNumber: ClassVar[int] = 138
    longName: ClassVar[str] = "JasPer License"
    licenseId: ClassVar[str] = "JasPer-2.0"
    seeAlso: ClassVar[List[str]] = ['http://www.ece.uvic.ca/~mdadams/jasper/LICENSE']
    isOsiApproved: ClassVar[bool] = False

class LicenseJplImage(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/JPL-image.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/JPL-image.json"
    referenceNumber: ClassVar[int] = 308
    longName: ClassVar[str] = "JPL Image Use Policy"
    licenseId: ClassVar[str] = "JPL-image"
    seeAlso: ClassVar[List[str]] = ['https://www.jpl.nasa.gov/jpl-image-use-policy']
    isOsiApproved: ClassVar[bool] = False

class LicenseJpnic(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/JPNIC.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/JPNIC.json"
    referenceNumber: ClassVar[int] = 118
    longName: ClassVar[str] = "Japan Network Information Center License"
    licenseId: ClassVar[str] = "JPNIC"
    seeAlso: ClassVar[List[str]] = ['https://gitlab.isc.org/isc-projects/bind9/blob/master/COPYRIGHT#L366']
    isOsiApproved: ClassVar[bool] = False

class LicenseJson(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/JSON.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/JSON.json"
    referenceNumber: ClassVar[int] = 68
    longName: ClassVar[str] = "JSON License"
    licenseId: ClassVar[str] = "JSON"
    seeAlso: ClassVar[List[str]] = ['http://www.json.org/license.html']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = False

class LicenseKastrup(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Kastrup.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Kastrup.json"
    referenceNumber: ClassVar[int] = 416
    longName: ClassVar[str] = "Kastrup License"
    licenseId: ClassVar[str] = "Kastrup"
    seeAlso: ClassVar[List[str]] = ['https://ctan.math.utah.edu/ctan/tex-archive/macros/generic/kastrup/binhex.dtx']
    isOsiApproved: ClassVar[bool] = False

class LicenseKazlib(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Kazlib.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Kazlib.json"
    referenceNumber: ClassVar[int] = 162
    longName: ClassVar[str] = "Kazlib License"
    licenseId: ClassVar[str] = "Kazlib"
    seeAlso: ClassVar[List[str]] = ['http://git.savannah.gnu.org/cgit/kazlib.git/tree/except.c?id=0062df360c2d17d57f6af19b0e444c51feb99036']
    isOsiApproved: ClassVar[bool] = False

class LicenseKnuthCtan(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Knuth-CTAN.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Knuth-CTAN.json"
    referenceNumber: ClassVar[int] = 387
    longName: ClassVar[str] = "Knuth CTAN License"
    licenseId: ClassVar[str] = "Knuth-CTAN"
    seeAlso: ClassVar[List[str]] = ['https://ctan.org/license/knuth']
    isOsiApproved: ClassVar[bool] = False

class LicenseLal1_2(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LAL-1.2.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LAL-1.2.json"
    referenceNumber: ClassVar[int] = 208
    longName: ClassVar[str] = "Licence Art Libre 1.2"
    licenseId: ClassVar[str] = "LAL-1.2"
    seeAlso: ClassVar[List[str]] = ['http://artlibre.org/licence/lal/licence-art-libre-12/']
    isOsiApproved: ClassVar[bool] = False

class LicenseLal1_3(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LAL-1.3.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LAL-1.3.json"
    referenceNumber: ClassVar[int] = 397
    longName: ClassVar[str] = "Licence Art Libre 1.3"
    licenseId: ClassVar[str] = "LAL-1.3"
    seeAlso: ClassVar[List[str]] = ['https://artlibre.org/']
    isOsiApproved: ClassVar[bool] = False

class LicenseLatex2e(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Latex2e.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Latex2e.json"
    referenceNumber: ClassVar[int] = 14
    longName: ClassVar[str] = "Latex2e License"
    licenseId: ClassVar[str] = "Latex2e"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Latex2e']
    isOsiApproved: ClassVar[bool] = False

class LicenseLatex2eTranslatedNotice(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Latex2e-translated-notice.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Latex2e-translated-notice.json"
    referenceNumber: ClassVar[int] = 33
    longName: ClassVar[str] = "Latex2e with translated notice permission"
    licenseId: ClassVar[str] = "Latex2e-translated-notice"
    seeAlso: ClassVar[List[str]] = ['https://git.savannah.gnu.org/cgit/indent.git/tree/doc/indent.texi?id=a74c6b4ee49397cf330b333da1042bffa60ed14f#n74']
    isOsiApproved: ClassVar[bool] = False

class LicenseLeptonica(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Leptonica.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Leptonica.json"
    referenceNumber: ClassVar[int] = 20
    longName: ClassVar[str] = "Leptonica License"
    licenseId: ClassVar[str] = "Leptonica"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Leptonica']
    isOsiApproved: ClassVar[bool] = False

class LicenseLgpl2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LGPL-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LGPL-2.0.json"
    referenceNumber: ClassVar[int] = 414
    longName: ClassVar[str] = "GNU Library General Public License v2 only"
    licenseId: ClassVar[str] = "LGPL-2.0"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/lgpl-2.0-standalone.html']
    isOsiApproved: ClassVar[bool] = True

class LicenseLgpl2_0Plus(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LGPL-2.0+.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LGPL-2.0+.json"
    referenceNumber: ClassVar[int] = 243
    longName: ClassVar[str] = "GNU Library General Public License v2 or later"
    licenseId: ClassVar[str] = "LGPL-2.0+"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/lgpl-2.0-standalone.html']
    isOsiApproved: ClassVar[bool] = True

class LicenseLgpl2_0Only(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LGPL-2.0-only.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LGPL-2.0-only.json"
    referenceNumber: ClassVar[int] = 461
    longName: ClassVar[str] = "GNU Library General Public License v2 only"
    licenseId: ClassVar[str] = "LGPL-2.0-only"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/lgpl-2.0-standalone.html']
    isOsiApproved: ClassVar[bool] = True

class LicenseLgpl2_0OrLater(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LGPL-2.0-or-later.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LGPL-2.0-or-later.json"
    referenceNumber: ClassVar[int] = 64
    longName: ClassVar[str] = "GNU Library General Public License v2 or later"
    licenseId: ClassVar[str] = "LGPL-2.0-or-later"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/lgpl-2.0-standalone.html']
    isOsiApproved: ClassVar[bool] = True

class LicenseLgpl2_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LGPL-2.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LGPL-2.1.json"
    referenceNumber: ClassVar[int] = 571
    longName: ClassVar[str] = "GNU Lesser General Public License v2.1 only"
    licenseId: ClassVar[str] = "LGPL-2.1"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/lgpl-2.1-standalone.html', 'https://opensource.org/licenses/LGPL-2.1']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseLgpl2_1Plus(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LGPL-2.1+.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LGPL-2.1+.json"
    referenceNumber: ClassVar[int] = 159
    longName: ClassVar[str] = "GNU Lesser General Public License v2.1 or later"
    licenseId: ClassVar[str] = "LGPL-2.1+"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/lgpl-2.1-standalone.html', 'https://opensource.org/licenses/LGPL-2.1']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseLgpl2_1Only(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LGPL-2.1-only.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LGPL-2.1-only.json"
    referenceNumber: ClassVar[int] = 481
    longName: ClassVar[str] = "GNU Lesser General Public License v2.1 only"
    licenseId: ClassVar[str] = "LGPL-2.1-only"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/lgpl-2.1-standalone.html', 'https://opensource.org/licenses/LGPL-2.1']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseLgpl2_1OrLater(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LGPL-2.1-or-later.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LGPL-2.1-or-later.json"
    referenceNumber: ClassVar[int] = 277
    longName: ClassVar[str] = "GNU Lesser General Public License v2.1 or later"
    licenseId: ClassVar[str] = "LGPL-2.1-or-later"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/old-licenses/lgpl-2.1-standalone.html', 'https://opensource.org/licenses/LGPL-2.1']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseLgpl3_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LGPL-3.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LGPL-3.0.json"
    referenceNumber: ClassVar[int] = 37
    longName: ClassVar[str] = "GNU Lesser General Public License v3.0 only"
    licenseId: ClassVar[str] = "LGPL-3.0"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/lgpl-3.0-standalone.html', 'https://www.gnu.org/licenses/lgpl+gpl-3.0.txt', 'https://opensource.org/licenses/LGPL-3.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseLgpl3_0Plus(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LGPL-3.0+.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LGPL-3.0+.json"
    referenceNumber: ClassVar[int] = 570
    longName: ClassVar[str] = "GNU Lesser General Public License v3.0 or later"
    licenseId: ClassVar[str] = "LGPL-3.0+"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/lgpl-3.0-standalone.html', 'https://www.gnu.org/licenses/lgpl+gpl-3.0.txt', 'https://opensource.org/licenses/LGPL-3.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseLgpl3_0Only(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LGPL-3.0-only.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LGPL-3.0-only.json"
    referenceNumber: ClassVar[int] = 106
    longName: ClassVar[str] = "GNU Lesser General Public License v3.0 only"
    licenseId: ClassVar[str] = "LGPL-3.0-only"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/lgpl-3.0-standalone.html', 'https://www.gnu.org/licenses/lgpl+gpl-3.0.txt', 'https://opensource.org/licenses/LGPL-3.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseLgpl3_0OrLater(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LGPL-3.0-or-later.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LGPL-3.0-or-later.json"
    referenceNumber: ClassVar[int] = 552
    longName: ClassVar[str] = "GNU Lesser General Public License v3.0 or later"
    licenseId: ClassVar[str] = "LGPL-3.0-or-later"
    seeAlso: ClassVar[List[str]] = ['https://www.gnu.org/licenses/lgpl-3.0-standalone.html', 'https://www.gnu.org/licenses/lgpl+gpl-3.0.txt', 'https://opensource.org/licenses/LGPL-3.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseLgpllr(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LGPLLR.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LGPLLR.json"
    referenceNumber: ClassVar[int] = 568
    longName: ClassVar[str] = "Lesser General Public License For Linguistic Resources"
    licenseId: ClassVar[str] = "LGPLLR"
    seeAlso: ClassVar[List[str]] = ['http://www-igm.univ-mlv.fr/~unitex/lgpllr.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseLibpng(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Libpng.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Libpng.json"
    referenceNumber: ClassVar[int] = 201
    longName: ClassVar[str] = "libpng License"
    licenseId: ClassVar[str] = "Libpng"
    seeAlso: ClassVar[List[str]] = ['http://www.libpng.org/pub/png/src/libpng-LICENSE.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseLibpng2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/libpng-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/libpng-2.0.json"
    referenceNumber: ClassVar[int] = 104
    longName: ClassVar[str] = "PNG Reference Library version 2"
    licenseId: ClassVar[str] = "libpng-2.0"
    seeAlso: ClassVar[List[str]] = ['http://www.libpng.org/pub/png/src/libpng-LICENSE.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseLibselinux1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/libselinux-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/libselinux-1.0.json"
    referenceNumber: ClassVar[int] = 220
    longName: ClassVar[str] = "libselinux public domain notice"
    licenseId: ClassVar[str] = "libselinux-1.0"
    seeAlso: ClassVar[List[str]] = ['https://github.com/SELinuxProject/selinux/blob/master/libselinux/LICENSE']
    isOsiApproved: ClassVar[bool] = False

class LicenseLibtiff(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/libtiff.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/libtiff.json"
    referenceNumber: ClassVar[int] = 143
    longName: ClassVar[str] = "libtiff License"
    licenseId: ClassVar[str] = "libtiff"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/libtiff']
    isOsiApproved: ClassVar[bool] = False

class LicenseLibutilDavidNugent(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/libutil-David-Nugent.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/libutil-David-Nugent.json"
    referenceNumber: ClassVar[int] = 526
    longName: ClassVar[str] = "libutil David Nugent License"
    licenseId: ClassVar[str] = "libutil-David-Nugent"
    seeAlso: ClassVar[List[str]] = ['http://web.mit.edu/freebsd/head/lib/libutil/login_ok.3', 'https://cgit.freedesktop.org/libbsd/tree/man/setproctitle.3bsd']
    isOsiApproved: ClassVar[bool] = False

class LicenseLiliqP1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LiLiQ-P-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LiLiQ-P-1.1.json"
    referenceNumber: ClassVar[int] = 58
    longName: ClassVar[str] = "Licence Libre du Québec – Permissive version 1.1"
    licenseId: ClassVar[str] = "LiLiQ-P-1.1"
    seeAlso: ClassVar[List[str]] = ['https://forge.gouv.qc.ca/licence/fr/liliq-v1-1/', 'http://opensource.org/licenses/LiLiQ-P-1.1']
    isOsiApproved: ClassVar[bool] = True

class LicenseLiliqR1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LiLiQ-R-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LiLiQ-R-1.1.json"
    referenceNumber: ClassVar[int] = 564
    longName: ClassVar[str] = "Licence Libre du Québec – Réciprocité version 1.1"
    licenseId: ClassVar[str] = "LiLiQ-R-1.1"
    seeAlso: ClassVar[List[str]] = ['https://www.forge.gouv.qc.ca/participez/licence-logicielle/licence-libre-du-quebec-liliq-en-francais/licence-libre-du-quebec-reciprocite-liliq-r-v1-1/', 'http://opensource.org/licenses/LiLiQ-R-1.1']
    isOsiApproved: ClassVar[bool] = True

class LicenseLiliqRplus1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LiLiQ-Rplus-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LiLiQ-Rplus-1.1.json"
    referenceNumber: ClassVar[int] = 47
    longName: ClassVar[str] = "Licence Libre du Québec – Réciprocité forte version 1.1"
    licenseId: ClassVar[str] = "LiLiQ-Rplus-1.1"
    seeAlso: ClassVar[List[str]] = ['https://www.forge.gouv.qc.ca/participez/licence-logicielle/licence-libre-du-quebec-liliq-en-francais/licence-libre-du-quebec-reciprocite-forte-liliq-r-v1-1/', 'http://opensource.org/licenses/LiLiQ-Rplus-1.1']
    isOsiApproved: ClassVar[bool] = True

class LicenseLinuxManPages1Para(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Linux-man-pages-1-para.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Linux-man-pages-1-para.json"
    referenceNumber: ClassVar[int] = 317
    longName: ClassVar[str] = "Linux man-pages - 1 paragraph"
    licenseId: ClassVar[str] = "Linux-man-pages-1-para"
    seeAlso: ClassVar[List[str]] = ['https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man2/getcpu.2#n4']
    isOsiApproved: ClassVar[bool] = False

class LicenseLinuxManPagesCopyleft(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Linux-man-pages-copyleft.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Linux-man-pages-copyleft.json"
    referenceNumber: ClassVar[int] = 150
    longName: ClassVar[str] = "Linux man-pages Copyleft"
    licenseId: ClassVar[str] = "Linux-man-pages-copyleft"
    seeAlso: ClassVar[List[str]] = ['https://www.kernel.org/doc/man-pages/licenses.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseLinuxManPagesCopyleft2Para(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Linux-man-pages-copyleft-2-para.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Linux-man-pages-copyleft-2-para.json"
    referenceNumber: ClassVar[int] = 511
    longName: ClassVar[str] = "Linux man-pages Copyleft - 2 paragraphs"
    licenseId: ClassVar[str] = "Linux-man-pages-copyleft-2-para"
    seeAlso: ClassVar[List[str]] = ['https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man2/move_pages.2#n5', 'https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man2/migrate_pages.2#n8']
    isOsiApproved: ClassVar[bool] = False

class LicenseLinuxManPagesCopyleftVar(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Linux-man-pages-copyleft-var.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Linux-man-pages-copyleft-var.json"
    referenceNumber: ClassVar[int] = 517
    longName: ClassVar[str] = "Linux man-pages Copyleft Variant"
    licenseId: ClassVar[str] = "Linux-man-pages-copyleft-var"
    seeAlso: ClassVar[List[str]] = ['https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/man2/set_mempolicy.2#n5']
    isOsiApproved: ClassVar[bool] = False

class LicenseLinuxOpenib(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Linux-OpenIB.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Linux-OpenIB.json"
    referenceNumber: ClassVar[int] = 559
    longName: ClassVar[str] = "Linux Kernel Variant of OpenIB.org license"
    licenseId: ClassVar[str] = "Linux-OpenIB"
    seeAlso: ClassVar[List[str]] = ['https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/infiniband/core/sa.h']
    isOsiApproved: ClassVar[bool] = False

class LicenseLoop(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LOOP.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LOOP.json"
    referenceNumber: ClassVar[int] = 458
    longName: ClassVar[str] = "Common Lisp LOOP License"
    licenseId: ClassVar[str] = "LOOP"
    seeAlso: ClassVar[List[str]] = ['https://gitlab.com/embeddable-common-lisp/ecl/-/blob/develop/src/lsp/loop.lsp', 'http://git.savannah.gnu.org/cgit/gcl.git/tree/gcl/lsp/gcl_loop.lsp?h=Version_2_6_13pre', 'https://sourceforge.net/p/sbcl/sbcl/ci/master/tree/src/code/loop.lisp', 'https://github.com/cl-adams/adams/blob/master/LICENSE.md', 'https://github.com/blakemcbride/eclipse-lisp/blob/master/lisp/loop.lisp', 'https://gitlab.common-lisp.net/cmucl/cmucl/-/blob/master/src/code/loop.lisp']
    isOsiApproved: ClassVar[bool] = False

class LicenseLpl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LPL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LPL-1.0.json"
    referenceNumber: ClassVar[int] = 349
    longName: ClassVar[str] = "Lucent Public License Version 1.0"
    licenseId: ClassVar[str] = "LPL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/LPL-1.0']
    isOsiApproved: ClassVar[bool] = True

class LicenseLpl1_02(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LPL-1.02.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LPL-1.02.json"
    referenceNumber: ClassVar[int] = 240
    longName: ClassVar[str] = "Lucent Public License v1.02"
    licenseId: ClassVar[str] = "LPL-1.02"
    seeAlso: ClassVar[List[str]] = ['http://plan9.bell-labs.com/plan9/license.html', 'https://opensource.org/licenses/LPL-1.02']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseLppl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LPPL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LPPL-1.0.json"
    referenceNumber: ClassVar[int] = 503
    longName: ClassVar[str] = "LaTeX Project Public License v1.0"
    licenseId: ClassVar[str] = "LPPL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://www.latex-project.org/lppl/lppl-1-0.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseLppl1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LPPL-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LPPL-1.1.json"
    referenceNumber: ClassVar[int] = 371
    longName: ClassVar[str] = "LaTeX Project Public License v1.1"
    licenseId: ClassVar[str] = "LPPL-1.1"
    seeAlso: ClassVar[List[str]] = ['http://www.latex-project.org/lppl/lppl-1-1.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseLppl1_2(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LPPL-1.2.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LPPL-1.2.json"
    referenceNumber: ClassVar[int] = 157
    longName: ClassVar[str] = "LaTeX Project Public License v1.2"
    licenseId: ClassVar[str] = "LPPL-1.2"
    seeAlso: ClassVar[List[str]] = ['http://www.latex-project.org/lppl/lppl-1-2.txt']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseLppl1_3a(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LPPL-1.3a.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LPPL-1.3a.json"
    referenceNumber: ClassVar[int] = 39
    longName: ClassVar[str] = "LaTeX Project Public License v1.3a"
    licenseId: ClassVar[str] = "LPPL-1.3a"
    seeAlso: ClassVar[List[str]] = ['http://www.latex-project.org/lppl/lppl-1-3a.txt']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseLppl1_3c(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LPPL-1.3c.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LPPL-1.3c.json"
    referenceNumber: ClassVar[int] = 2
    longName: ClassVar[str] = "LaTeX Project Public License v1.3c"
    licenseId: ClassVar[str] = "LPPL-1.3c"
    seeAlso: ClassVar[List[str]] = ['http://www.latex-project.org/lppl/lppl-1-3c.txt', 'https://opensource.org/licenses/LPPL-1.3c']
    isOsiApproved: ClassVar[bool] = True

class LicenseLsof(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/lsof.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/lsof.json"
    referenceNumber: ClassVar[int] = 153
    longName: ClassVar[str] = "lsof License"
    licenseId: ClassVar[str] = "lsof"
    seeAlso: ClassVar[List[str]] = ['https://github.com/lsof-org/lsof/blob/master/COPYING']
    isOsiApproved: ClassVar[bool] = False

class LicenseLucidaBitmapFonts(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Lucida-Bitmap-Fonts.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Lucida-Bitmap-Fonts.json"
    referenceNumber: ClassVar[int] = 420
    longName: ClassVar[str] = "Lucida Bitmap Fonts License"
    licenseId: ClassVar[str] = "Lucida-Bitmap-Fonts"
    seeAlso: ClassVar[List[str]] = ['https://gitlab.freedesktop.org/xorg/font/bh-100dpi/-/blob/master/COPYING?ref_type=heads']
    isOsiApproved: ClassVar[bool] = False

class LicenseLzmaSdk9_11To9_20(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LZMA-SDK-9.11-to-9.20.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LZMA-SDK-9.11-to-9.20.json"
    referenceNumber: ClassVar[int] = 288
    longName: ClassVar[str] = "LZMA SDK License (versions 9.11 to 9.20)"
    licenseId: ClassVar[str] = "LZMA-SDK-9.11-to-9.20"
    seeAlso: ClassVar[List[str]] = ['https://www.7-zip.org/sdk.html', 'https://sourceforge.net/projects/sevenzip/files/LZMA%20SDK/']
    isOsiApproved: ClassVar[bool] = False

class LicenseLzmaSdk9_22(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/LZMA-SDK-9.22.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/LZMA-SDK-9.22.json"
    referenceNumber: ClassVar[int] = 400
    longName: ClassVar[str] = "LZMA SDK License (versions 9.22 and beyond)"
    licenseId: ClassVar[str] = "LZMA-SDK-9.22"
    seeAlso: ClassVar[List[str]] = ['https://www.7-zip.org/sdk.html', 'https://sourceforge.net/projects/sevenzip/files/LZMA%20SDK/']
    isOsiApproved: ClassVar[bool] = False

class LicenseMagaz(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/magaz.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/magaz.json"
    referenceNumber: ClassVar[int] = 57
    longName: ClassVar[str] = "magaz License"
    licenseId: ClassVar[str] = "magaz"
    seeAlso: ClassVar[List[str]] = ['https://mirrors.nic.cz/tex-archive/macros/latex/contrib/magaz/magaz.tex']
    isOsiApproved: ClassVar[bool] = False

class LicenseMakeindex(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MakeIndex.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MakeIndex.json"
    referenceNumber: ClassVar[int] = 163
    longName: ClassVar[str] = "MakeIndex License"
    licenseId: ClassVar[str] = "MakeIndex"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/MakeIndex']
    isOsiApproved: ClassVar[bool] = False

class LicenseMartinBirgmeier(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Martin-Birgmeier.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Martin-Birgmeier.json"
    referenceNumber: ClassVar[int] = 369
    longName: ClassVar[str] = "Martin Birgmeier License"
    licenseId: ClassVar[str] = "Martin-Birgmeier"
    seeAlso: ClassVar[List[str]] = ['https://github.com/Perl/perl5/blob/blead/util.c#L6136']
    isOsiApproved: ClassVar[bool] = False

class LicenseMcpheeSlideshow(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/McPhee-slideshow.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/McPhee-slideshow.json"
    referenceNumber: ClassVar[int] = 359
    longName: ClassVar[str] = "McPhee Slideshow License"
    licenseId: ClassVar[str] = "McPhee-slideshow"
    seeAlso: ClassVar[List[str]] = ['https://mirror.las.iastate.edu/tex-archive/graphics/metapost/contrib/macros/slideshow/slideshow.mp']
    isOsiApproved: ClassVar[bool] = False

class LicenseMetamail(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/metamail.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/metamail.json"
    referenceNumber: ClassVar[int] = 175
    longName: ClassVar[str] = "metamail License"
    licenseId: ClassVar[str] = "metamail"
    seeAlso: ClassVar[List[str]] = ['https://github.com/Dual-Life/mime-base64/blob/master/Base64.xs#L12']
    isOsiApproved: ClassVar[bool] = False

class LicenseMinpack(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Minpack.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Minpack.json"
    referenceNumber: ClassVar[int] = 605
    longName: ClassVar[str] = "Minpack License"
    licenseId: ClassVar[str] = "Minpack"
    seeAlso: ClassVar[List[str]] = ['http://www.netlib.org/minpack/disclaimer', 'https://gitlab.com/libeigen/eigen/-/blob/master/COPYING.MINPACK']
    isOsiApproved: ClassVar[bool] = False

class LicenseMiros(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MirOS.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MirOS.json"
    referenceNumber: ClassVar[int] = 155
    longName: ClassVar[str] = "The MirOS Licence"
    licenseId: ClassVar[str] = "MirOS"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/MirOS']
    isOsiApproved: ClassVar[bool] = True

class LicenseMit(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MIT.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MIT.json"
    referenceNumber: ClassVar[int] = 205
    longName: ClassVar[str] = "MIT License"
    licenseId: ClassVar[str] = "MIT"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/MIT']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseMit0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MIT-0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MIT-0.json"
    referenceNumber: ClassVar[int] = 338
    longName: ClassVar[str] = "MIT No Attribution"
    licenseId: ClassVar[str] = "MIT-0"
    seeAlso: ClassVar[List[str]] = ['https://github.com/aws/mit-0', 'https://romanrm.net/mit-zero', 'https://github.com/awsdocs/aws-cloud9-user-guide/blob/master/LICENSE-SAMPLECODE']
    isOsiApproved: ClassVar[bool] = True

class LicenseMitAdvertising(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MIT-advertising.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MIT-advertising.json"
    referenceNumber: ClassVar[int] = 269
    longName: ClassVar[str] = "Enlightenment License (e16)"
    licenseId: ClassVar[str] = "MIT-advertising"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/MIT_With_Advertising']
    isOsiApproved: ClassVar[bool] = False

class LicenseMitCmu(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MIT-CMU.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MIT-CMU.json"
    referenceNumber: ClassVar[int] = 324
    longName: ClassVar[str] = "CMU License"
    licenseId: ClassVar[str] = "MIT-CMU"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing:MIT?rd=Licensing/MIT#CMU_Style', 'https://github.com/python-pillow/Pillow/blob/fffb426092c8db24a5f4b6df243a8a3c01fb63cd/LICENSE']
    isOsiApproved: ClassVar[bool] = False

class LicenseMitEnna(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MIT-enna.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MIT-enna.json"
    referenceNumber: ClassVar[int] = 256
    longName: ClassVar[str] = "enna License"
    licenseId: ClassVar[str] = "MIT-enna"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/MIT#enna']
    isOsiApproved: ClassVar[bool] = False

class LicenseMitFeh(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MIT-feh.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MIT-feh.json"
    referenceNumber: ClassVar[int] = 274
    longName: ClassVar[str] = "feh License"
    licenseId: ClassVar[str] = "MIT-feh"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/MIT#feh']
    isOsiApproved: ClassVar[bool] = False

class LicenseMitFestival(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MIT-Festival.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MIT-Festival.json"
    referenceNumber: ClassVar[int] = 326
    longName: ClassVar[str] = "MIT Festival Variant"
    licenseId: ClassVar[str] = "MIT-Festival"
    seeAlso: ClassVar[List[str]] = ['https://github.com/festvox/flite/blob/master/COPYING', 'https://github.com/festvox/speech_tools/blob/master/COPYING']
    isOsiApproved: ClassVar[bool] = False

class LicenseMitModernVariant(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MIT-Modern-Variant.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MIT-Modern-Variant.json"
    referenceNumber: ClassVar[int] = 466
    longName: ClassVar[str] = "MIT License Modern Variant"
    licenseId: ClassVar[str] = "MIT-Modern-Variant"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing:MIT#Modern_Variants', 'https://ptolemy.berkeley.edu/copyright.htm', 'https://pirlwww.lpl.arizona.edu/resources/guide/software/PerlTk/Tixlic.html']
    isOsiApproved: ClassVar[bool] = True

class LicenseMitOpenGroup(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MIT-open-group.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MIT-open-group.json"
    referenceNumber: ClassVar[int] = 221
    longName: ClassVar[str] = "MIT Open Group variant"
    licenseId: ClassVar[str] = "MIT-open-group"
    seeAlso: ClassVar[List[str]] = ['https://gitlab.freedesktop.org/xorg/app/iceauth/-/blob/master/COPYING', 'https://gitlab.freedesktop.org/xorg/app/xvinfo/-/blob/master/COPYING', 'https://gitlab.freedesktop.org/xorg/app/xsetroot/-/blob/master/COPYING', 'https://gitlab.freedesktop.org/xorg/app/xauth/-/blob/master/COPYING']
    isOsiApproved: ClassVar[bool] = False

class LicenseMitTestregex(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MIT-testregex.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MIT-testregex.json"
    referenceNumber: ClassVar[int] = 100
    longName: ClassVar[str] = "MIT testregex Variant"
    licenseId: ClassVar[str] = "MIT-testregex"
    seeAlso: ClassVar[List[str]] = ['https://github.com/dotnet/runtime/blob/55e1ac7c07df62c4108d4acedf78f77574470ce5/src/libraries/System.Text.RegularExpressions/tests/FunctionalTests/AttRegexTests.cs#L12-L28']
    isOsiApproved: ClassVar[bool] = False

class LicenseMitWu(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MIT-Wu.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MIT-Wu.json"
    referenceNumber: ClassVar[int] = 364
    longName: ClassVar[str] = "MIT Tom Wu Variant"
    licenseId: ClassVar[str] = "MIT-Wu"
    seeAlso: ClassVar[List[str]] = ['https://github.com/chromium/octane/blob/master/crypto.js']
    isOsiApproved: ClassVar[bool] = False

class LicenseMitnfa(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MITNFA.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MITNFA.json"
    referenceNumber: ClassVar[int] = 65
    longName: ClassVar[str] = "MIT +no-false-attribs license"
    licenseId: ClassVar[str] = "MITNFA"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/MITNFA']
    isOsiApproved: ClassVar[bool] = False

class LicenseMmixware(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MMIXware.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MMIXware.json"
    referenceNumber: ClassVar[int] = 438
    longName: ClassVar[str] = "MMIXware License"
    licenseId: ClassVar[str] = "MMIXware"
    seeAlso: ClassVar[List[str]] = ['https://gitlab.lrz.de/mmix/mmixware/-/blob/master/boilerplate.w']
    isOsiApproved: ClassVar[bool] = False

class LicenseMotosoto(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Motosoto.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Motosoto.json"
    referenceNumber: ClassVar[int] = 226
    longName: ClassVar[str] = "Motosoto License"
    licenseId: ClassVar[str] = "Motosoto"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/Motosoto']
    isOsiApproved: ClassVar[bool] = True

class LicenseMpegSsg(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MPEG-SSG.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MPEG-SSG.json"
    referenceNumber: ClassVar[int] = 593
    longName: ClassVar[str] = "MPEG Software Simulation"
    licenseId: ClassVar[str] = "MPEG-SSG"
    seeAlso: ClassVar[List[str]] = ['https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/converter/ppm/ppmtompeg/jrevdct.c#l1189']
    isOsiApproved: ClassVar[bool] = False

class LicenseMpiPermissive(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/mpi-permissive.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/mpi-permissive.json"
    referenceNumber: ClassVar[int] = 72
    longName: ClassVar[str] = "mpi Permissive License"
    licenseId: ClassVar[str] = "mpi-permissive"
    seeAlso: ClassVar[List[str]] = ['https://sources.debian.org/src/openmpi/4.1.0-10/ompi/debuggers/msgq_interface.h/?hl=19#L19']
    isOsiApproved: ClassVar[bool] = False

class LicenseMpich2(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/mpich2.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/mpich2.json"
    referenceNumber: ClassVar[int] = 574
    longName: ClassVar[str] = "mpich2 License"
    licenseId: ClassVar[str] = "mpich2"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/MIT']
    isOsiApproved: ClassVar[bool] = False

class LicenseMpl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MPL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MPL-1.0.json"
    referenceNumber: ClassVar[int] = 395
    longName: ClassVar[str] = "Mozilla Public License 1.0"
    licenseId: ClassVar[str] = "MPL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://www.mozilla.org/MPL/MPL-1.0.html', 'https://opensource.org/licenses/MPL-1.0']
    isOsiApproved: ClassVar[bool] = True

class LicenseMpl1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MPL-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MPL-1.1.json"
    referenceNumber: ClassVar[int] = 350
    longName: ClassVar[str] = "Mozilla Public License 1.1"
    licenseId: ClassVar[str] = "MPL-1.1"
    seeAlso: ClassVar[List[str]] = ['http://www.mozilla.org/MPL/MPL-1.1.html', 'https://opensource.org/licenses/MPL-1.1']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseMpl2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MPL-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MPL-2.0.json"
    referenceNumber: ClassVar[int] = 586
    longName: ClassVar[str] = "Mozilla Public License 2.0"
    licenseId: ClassVar[str] = "MPL-2.0"
    seeAlso: ClassVar[List[str]] = ['https://www.mozilla.org/MPL/2.0/', 'https://opensource.org/licenses/MPL-2.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseMpl2_0NoCopyleftException(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MPL-2.0-no-copyleft-exception.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MPL-2.0-no-copyleft-exception.json"
    referenceNumber: ClassVar[int] = 225
    longName: ClassVar[str] = "Mozilla Public License 2.0 (no copyleft exception)"
    licenseId: ClassVar[str] = "MPL-2.0-no-copyleft-exception"
    seeAlso: ClassVar[List[str]] = ['https://www.mozilla.org/MPL/2.0/', 'https://opensource.org/licenses/MPL-2.0']
    isOsiApproved: ClassVar[bool] = True

class LicenseMplus(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/mplus.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/mplus.json"
    referenceNumber: ClassVar[int] = 491
    longName: ClassVar[str] = "mplus Font License"
    licenseId: ClassVar[str] = "mplus"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing:Mplus?rd=Licensing/mplus']
    isOsiApproved: ClassVar[bool] = False

class LicenseMsLpl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MS-LPL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MS-LPL.json"
    referenceNumber: ClassVar[int] = 360
    longName: ClassVar[str] = "Microsoft Limited Public License"
    licenseId: ClassVar[str] = "MS-LPL"
    seeAlso: ClassVar[List[str]] = ['https://www.openhub.net/licenses/mslpl', 'https://github.com/gabegundy/atlserver/blob/master/License.txt', 'https://en.wikipedia.org/wiki/Shared_Source_Initiative#Microsoft_Limited_Public_License_(Ms-LPL)']
    isOsiApproved: ClassVar[bool] = False

class LicenseMsPl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MS-PL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MS-PL.json"
    referenceNumber: ClassVar[int] = 437
    longName: ClassVar[str] = "Microsoft Public License"
    licenseId: ClassVar[str] = "MS-PL"
    seeAlso: ClassVar[List[str]] = ['http://www.microsoft.com/opensource/licenses.mspx', 'https://opensource.org/licenses/MS-PL']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseMsRl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MS-RL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MS-RL.json"
    referenceNumber: ClassVar[int] = 442
    longName: ClassVar[str] = "Microsoft Reciprocal License"
    licenseId: ClassVar[str] = "MS-RL"
    seeAlso: ClassVar[List[str]] = ['http://www.microsoft.com/opensource/licenses.mspx', 'https://opensource.org/licenses/MS-RL']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseMtll(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MTLL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MTLL.json"
    referenceNumber: ClassVar[int] = 555
    longName: ClassVar[str] = "Matrix Template Library License"
    licenseId: ClassVar[str] = "MTLL"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Matrix_Template_Library_License']
    isOsiApproved: ClassVar[bool] = False

class LicenseMulanpsl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MulanPSL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MulanPSL-1.0.json"
    referenceNumber: ClassVar[int] = 119
    longName: ClassVar[str] = "Mulan Permissive Software License, Version 1"
    licenseId: ClassVar[str] = "MulanPSL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://license.coscl.org.cn/MulanPSL/', 'https://github.com/yuwenlong/longphp/blob/25dfb70cc2a466dc4bb55ba30901cbce08d164b5/LICENSE']
    isOsiApproved: ClassVar[bool] = False

class LicenseMulanpsl2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/MulanPSL-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/MulanPSL-2.0.json"
    referenceNumber: ClassVar[int] = 144
    longName: ClassVar[str] = "Mulan Permissive Software License, Version 2"
    licenseId: ClassVar[str] = "MulanPSL-2.0"
    seeAlso: ClassVar[List[str]] = ['https://license.coscl.org.cn/MulanPSL2/']
    isOsiApproved: ClassVar[bool] = True

class LicenseMultics(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Multics.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Multics.json"
    referenceNumber: ClassVar[int] = 510
    longName: ClassVar[str] = "Multics License"
    licenseId: ClassVar[str] = "Multics"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/Multics']
    isOsiApproved: ClassVar[bool] = True

class LicenseMup(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Mup.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Mup.json"
    referenceNumber: ClassVar[int] = 290
    longName: ClassVar[str] = "Mup License"
    licenseId: ClassVar[str] = "Mup"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Mup']
    isOsiApproved: ClassVar[bool] = False

class LicenseNaist2003(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NAIST-2003.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NAIST-2003.json"
    referenceNumber: ClassVar[int] = 410
    longName: ClassVar[str] = "Nara Institute of Science and Technology License (2003)"
    licenseId: ClassVar[str] = "NAIST-2003"
    seeAlso: ClassVar[List[str]] = ['https://enterprise.dejacode.com/licenses/public/naist-2003/#license-text', 'https://github.com/nodejs/node/blob/4a19cc8947b1bba2b2d27816ec3d0edf9b28e503/LICENSE#L343']
    isOsiApproved: ClassVar[bool] = False

class LicenseNasa1_3(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NASA-1.3.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NASA-1.3.json"
    referenceNumber: ClassVar[int] = 525
    longName: ClassVar[str] = "NASA Open Source Agreement 1.3"
    licenseId: ClassVar[str] = "NASA-1.3"
    seeAlso: ClassVar[List[str]] = ['http://ti.arc.nasa.gov/opensource/nosa/', 'https://opensource.org/licenses/NASA-1.3']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = False

class LicenseNaumen(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Naumen.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Naumen.json"
    referenceNumber: ClassVar[int] = 230
    longName: ClassVar[str] = "Naumen Public License"
    licenseId: ClassVar[str] = "Naumen"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/Naumen']
    isOsiApproved: ClassVar[bool] = True

class LicenseNbpl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NBPL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NBPL-1.0.json"
    referenceNumber: ClassVar[int] = 135
    longName: ClassVar[str] = "Net Boolean Public License v1"
    licenseId: ClassVar[str] = "NBPL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=37b4b3f6cc4bf34e1d3dec61e69914b9819d8894']
    isOsiApproved: ClassVar[bool] = False

class LicenseNcglUk2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NCGL-UK-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NCGL-UK-2.0.json"
    referenceNumber: ClassVar[int] = 303
    longName: ClassVar[str] = "Non-Commercial Government Licence"
    licenseId: ClassVar[str] = "NCGL-UK-2.0"
    seeAlso: ClassVar[List[str]] = ['http://www.nationalarchives.gov.uk/doc/non-commercial-government-licence/version/2/']
    isOsiApproved: ClassVar[bool] = False

class LicenseNcsa(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NCSA.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NCSA.json"
    referenceNumber: ClassVar[int] = 299
    longName: ClassVar[str] = "University of Illinois/NCSA Open Source License"
    licenseId: ClassVar[str] = "NCSA"
    seeAlso: ClassVar[List[str]] = ['http://otm.illinois.edu/uiuc_openSource', 'https://opensource.org/licenses/NCSA']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseNetSnmp(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Net-SNMP.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Net-SNMP.json"
    referenceNumber: ClassVar[int] = 345
    longName: ClassVar[str] = "Net-SNMP License"
    licenseId: ClassVar[str] = "Net-SNMP"
    seeAlso: ClassVar[List[str]] = ['http://net-snmp.sourceforge.net/about/license.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseNetcdf(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NetCDF.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NetCDF.json"
    referenceNumber: ClassVar[int] = 351
    longName: ClassVar[str] = "NetCDF license"
    licenseId: ClassVar[str] = "NetCDF"
    seeAlso: ClassVar[List[str]] = ['http://www.unidata.ucar.edu/software/netcdf/copyright.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseNewsletr(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Newsletr.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Newsletr.json"
    referenceNumber: ClassVar[int] = 320
    longName: ClassVar[str] = "Newsletr License"
    licenseId: ClassVar[str] = "Newsletr"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Newsletr']
    isOsiApproved: ClassVar[bool] = False

class LicenseNgpl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NGPL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NGPL.json"
    referenceNumber: ClassVar[int] = 96
    longName: ClassVar[str] = "Nethack General Public License"
    licenseId: ClassVar[str] = "NGPL"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/NGPL']
    isOsiApproved: ClassVar[bool] = True

class LicenseNicta1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NICTA-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NICTA-1.0.json"
    referenceNumber: ClassVar[int] = 16
    longName: ClassVar[str] = "NICTA Public Software License, Version 1.0"
    licenseId: ClassVar[str] = "NICTA-1.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.apple.com/source/mDNSResponder/mDNSResponder-320.10/mDNSPosix/nss_ReadMe.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseNistPd(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NIST-PD.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NIST-PD.json"
    referenceNumber: ClassVar[int] = 94
    longName: ClassVar[str] = "NIST Public Domain Notice"
    licenseId: ClassVar[str] = "NIST-PD"
    seeAlso: ClassVar[List[str]] = ['https://github.com/tcheneau/simpleRPL/blob/e645e69e38dd4e3ccfeceb2db8cba05b7c2e0cd3/LICENSE.txt', 'https://github.com/tcheneau/Routing/blob/f09f46fcfe636107f22f2c98348188a65a135d98/README.md']
    isOsiApproved: ClassVar[bool] = False

class LicenseNistPdFallback(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NIST-PD-fallback.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NIST-PD-fallback.json"
    referenceNumber: ClassVar[int] = 329
    longName: ClassVar[str] = "NIST Public Domain Notice with license fallback"
    licenseId: ClassVar[str] = "NIST-PD-fallback"
    seeAlso: ClassVar[List[str]] = ['https://github.com/usnistgov/jsip/blob/59700e6926cbe96c5cdae897d9a7d2656b42abe3/LICENSE', 'https://github.com/usnistgov/fipy/blob/86aaa5c2ba2c6f1be19593c5986071cf6568cc34/LICENSE.rst']
    isOsiApproved: ClassVar[bool] = False

class LicenseNistSoftware(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NIST-Software.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NIST-Software.json"
    referenceNumber: ClassVar[int] = 218
    longName: ClassVar[str] = "NIST Software License"
    licenseId: ClassVar[str] = "NIST-Software"
    seeAlso: ClassVar[List[str]] = ['https://github.com/open-quantum-safe/liboqs/blob/40b01fdbb270f8614fde30e65d30e9da18c02393/src/common/rand/rand_nist.c#L1-L15']
    isOsiApproved: ClassVar[bool] = False

class LicenseNlod1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NLOD-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NLOD-1.0.json"
    referenceNumber: ClassVar[int] = 149
    longName: ClassVar[str] = "Norwegian Licence for Open Government Data (NLOD) 1.0"
    licenseId: ClassVar[str] = "NLOD-1.0"
    seeAlso: ClassVar[List[str]] = ['http://data.norge.no/nlod/en/1.0']
    isOsiApproved: ClassVar[bool] = False

class LicenseNlod2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NLOD-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NLOD-2.0.json"
    referenceNumber: ClassVar[int] = 128
    longName: ClassVar[str] = "Norwegian Licence for Open Government Data (NLOD) 2.0"
    licenseId: ClassVar[str] = "NLOD-2.0"
    seeAlso: ClassVar[List[str]] = ['http://data.norge.no/nlod/en/2.0']
    isOsiApproved: ClassVar[bool] = False

class LicenseNlpl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NLPL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NLPL.json"
    referenceNumber: ClassVar[int] = 74
    longName: ClassVar[str] = "No Limit Public License"
    licenseId: ClassVar[str] = "NLPL"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/NLPL']
    isOsiApproved: ClassVar[bool] = False

class LicenseNokia(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Nokia.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Nokia.json"
    referenceNumber: ClassVar[int] = 134
    longName: ClassVar[str] = "Nokia Open Source License"
    licenseId: ClassVar[str] = "Nokia"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/nokia']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseNosl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NOSL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NOSL.json"
    referenceNumber: ClassVar[int] = 103
    longName: ClassVar[str] = "Netizen Open Source License"
    licenseId: ClassVar[str] = "NOSL"
    seeAlso: ClassVar[List[str]] = ['http://bits.netizen.com.au/licenses/NOSL/nosl.txt']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseNoweb(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Noweb.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Noweb.json"
    referenceNumber: ClassVar[int] = 244
    longName: ClassVar[str] = "Noweb License"
    licenseId: ClassVar[str] = "Noweb"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Noweb']
    isOsiApproved: ClassVar[bool] = False

class LicenseNpl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NPL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NPL-1.0.json"
    referenceNumber: ClassVar[int] = 207
    longName: ClassVar[str] = "Netscape Public License v1.0"
    licenseId: ClassVar[str] = "NPL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://www.mozilla.org/MPL/NPL/1.0/']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseNpl1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NPL-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NPL-1.1.json"
    referenceNumber: ClassVar[int] = 148
    longName: ClassVar[str] = "Netscape Public License v1.1"
    licenseId: ClassVar[str] = "NPL-1.1"
    seeAlso: ClassVar[List[str]] = ['http://www.mozilla.org/MPL/NPL/1.1/']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseNposl3_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NPOSL-3.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NPOSL-3.0.json"
    referenceNumber: ClassVar[int] = 604
    longName: ClassVar[str] = "Non-Profit Open Software License 3.0"
    licenseId: ClassVar[str] = "NPOSL-3.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/NOSL3.0']
    isOsiApproved: ClassVar[bool] = True

class LicenseNrl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NRL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NRL.json"
    referenceNumber: ClassVar[int] = 540
    longName: ClassVar[str] = "NRL License"
    licenseId: ClassVar[str] = "NRL"
    seeAlso: ClassVar[List[str]] = ['http://web.mit.edu/network/isakmp/nrllicense.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseNtp(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NTP.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NTP.json"
    referenceNumber: ClassVar[int] = 0
    longName: ClassVar[str] = "NTP License"
    licenseId: ClassVar[str] = "NTP"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/NTP']
    isOsiApproved: ClassVar[bool] = True

class LicenseNtp0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/NTP-0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/NTP-0.json"
    referenceNumber: ClassVar[int] = 71
    longName: ClassVar[str] = "NTP No Attribution"
    licenseId: ClassVar[str] = "NTP-0"
    seeAlso: ClassVar[List[str]] = ['https://github.com/tytso/e2fsprogs/blob/master/lib/et/et_name.c']
    isOsiApproved: ClassVar[bool] = False

class LicenseNunit(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Nunit.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Nunit.json"
    referenceNumber: ClassVar[int] = 428
    longName: ClassVar[str] = "Nunit License"
    licenseId: ClassVar[str] = "Nunit"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Nunit']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseOUda1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/O-UDA-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/O-UDA-1.0.json"
    referenceNumber: ClassVar[int] = 545
    longName: ClassVar[str] = "Open Use of Data Agreement v1.0"
    licenseId: ClassVar[str] = "O-UDA-1.0"
    seeAlso: ClassVar[List[str]] = ['https://github.com/microsoft/Open-Use-of-Data-Agreement/blob/v1.0/O-UDA-1.0.md', 'https://cdla.dev/open-use-of-data-agreement-v1-0/']
    isOsiApproved: ClassVar[bool] = False

class LicenseOcctPl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OCCT-PL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OCCT-PL.json"
    referenceNumber: ClassVar[int] = 476
    longName: ClassVar[str] = "Open CASCADE Technology Public License"
    licenseId: ClassVar[str] = "OCCT-PL"
    seeAlso: ClassVar[List[str]] = ['http://www.opencascade.com/content/occt-public-license']
    isOsiApproved: ClassVar[bool] = False

class LicenseOclc2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OCLC-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OCLC-2.0.json"
    referenceNumber: ClassVar[int] = 285
    longName: ClassVar[str] = "OCLC Research Public License 2.0"
    licenseId: ClassVar[str] = "OCLC-2.0"
    seeAlso: ClassVar[List[str]] = ['http://www.oclc.org/research/activities/software/license/v2final.htm', 'https://opensource.org/licenses/OCLC-2.0']
    isOsiApproved: ClassVar[bool] = True

class LicenseOdbl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/ODbL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/ODbL-1.0.json"
    referenceNumber: ClassVar[int] = 533
    longName: ClassVar[str] = "Open Data Commons Open Database License v1.0"
    licenseId: ClassVar[str] = "ODbL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://www.opendatacommons.org/licenses/odbl/1.0/', 'https://opendatacommons.org/licenses/odbl/1-0/']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseOdcBy1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/ODC-By-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/ODC-By-1.0.json"
    referenceNumber: ClassVar[int] = 176
    longName: ClassVar[str] = "Open Data Commons Attribution License v1.0"
    licenseId: ClassVar[str] = "ODC-By-1.0"
    seeAlso: ClassVar[List[str]] = ['https://opendatacommons.org/licenses/by/1.0/']
    isOsiApproved: ClassVar[bool] = False

class LicenseOffis(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OFFIS.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OFFIS.json"
    referenceNumber: ClassVar[int] = 116
    longName: ClassVar[str] = "OFFIS License"
    licenseId: ClassVar[str] = "OFFIS"
    seeAlso: ClassVar[List[str]] = ['https://sourceforge.net/p/xmedcon/code/ci/master/tree/libs/dicom/README']
    isOsiApproved: ClassVar[bool] = False

class LicenseOfl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OFL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OFL-1.0.json"
    referenceNumber: ClassVar[int] = 295
    longName: ClassVar[str] = "SIL Open Font License 1.0"
    licenseId: ClassVar[str] = "OFL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://scripts.sil.org/cms/scripts/page.php?item_id=OFL10_web']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseOfl1_0NoRfn(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OFL-1.0-no-RFN.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OFL-1.0-no-RFN.json"
    referenceNumber: ClassVar[int] = 504
    longName: ClassVar[str] = "SIL Open Font License 1.0 with no Reserved Font Name"
    licenseId: ClassVar[str] = "OFL-1.0-no-RFN"
    seeAlso: ClassVar[List[str]] = ['http://scripts.sil.org/cms/scripts/page.php?item_id=OFL10_web']
    isOsiApproved: ClassVar[bool] = False

class LicenseOfl1_0Rfn(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OFL-1.0-RFN.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OFL-1.0-RFN.json"
    referenceNumber: ClassVar[int] = 250
    longName: ClassVar[str] = "SIL Open Font License 1.0 with Reserved Font Name"
    licenseId: ClassVar[str] = "OFL-1.0-RFN"
    seeAlso: ClassVar[List[str]] = ['http://scripts.sil.org/cms/scripts/page.php?item_id=OFL10_web']
    isOsiApproved: ClassVar[bool] = False

class LicenseOfl1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OFL-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OFL-1.1.json"
    referenceNumber: ClassVar[int] = 433
    longName: ClassVar[str] = "SIL Open Font License 1.1"
    licenseId: ClassVar[str] = "OFL-1.1"
    seeAlso: ClassVar[List[str]] = ['http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web', 'https://opensource.org/licenses/OFL-1.1']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseOfl1_1NoRfn(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OFL-1.1-no-RFN.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OFL-1.1-no-RFN.json"
    referenceNumber: ClassVar[int] = 186
    longName: ClassVar[str] = "SIL Open Font License 1.1 with no Reserved Font Name"
    licenseId: ClassVar[str] = "OFL-1.1-no-RFN"
    seeAlso: ClassVar[List[str]] = ['http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web', 'https://opensource.org/licenses/OFL-1.1']
    isOsiApproved: ClassVar[bool] = True

class LicenseOfl1_1Rfn(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OFL-1.1-RFN.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OFL-1.1-RFN.json"
    referenceNumber: ClassVar[int] = 558
    longName: ClassVar[str] = "SIL Open Font License 1.1 with Reserved Font Name"
    licenseId: ClassVar[str] = "OFL-1.1-RFN"
    seeAlso: ClassVar[List[str]] = ['http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web', 'https://opensource.org/licenses/OFL-1.1']
    isOsiApproved: ClassVar[bool] = True

class LicenseOgc1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OGC-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OGC-1.0.json"
    referenceNumber: ClassVar[int] = 515
    longName: ClassVar[str] = "OGC Software License, Version 1.0"
    licenseId: ClassVar[str] = "OGC-1.0"
    seeAlso: ClassVar[List[str]] = ['https://www.ogc.org/ogc/software/1.0']
    isOsiApproved: ClassVar[bool] = False

class LicenseOgdlTaiwan1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OGDL-Taiwan-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OGDL-Taiwan-1.0.json"
    referenceNumber: ClassVar[int] = 547
    longName: ClassVar[str] = "Taiwan Open Government Data License, version 1.0"
    licenseId: ClassVar[str] = "OGDL-Taiwan-1.0"
    seeAlso: ClassVar[List[str]] = ['https://data.gov.tw/license']
    isOsiApproved: ClassVar[bool] = False

class LicenseOglCanada2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OGL-Canada-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OGL-Canada-2.0.json"
    referenceNumber: ClassVar[int] = 146
    longName: ClassVar[str] = "Open Government Licence - Canada"
    licenseId: ClassVar[str] = "OGL-Canada-2.0"
    seeAlso: ClassVar[List[str]] = ['https://open.canada.ca/en/open-government-licence-canada']
    isOsiApproved: ClassVar[bool] = False

class LicenseOglUk1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OGL-UK-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OGL-UK-1.0.json"
    referenceNumber: ClassVar[int] = 347
    longName: ClassVar[str] = "Open Government Licence v1.0"
    licenseId: ClassVar[str] = "OGL-UK-1.0"
    seeAlso: ClassVar[List[str]] = ['http://www.nationalarchives.gov.uk/doc/open-government-licence/version/1/']
    isOsiApproved: ClassVar[bool] = False

class LicenseOglUk2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OGL-UK-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OGL-UK-2.0.json"
    referenceNumber: ClassVar[int] = 588
    longName: ClassVar[str] = "Open Government Licence v2.0"
    licenseId: ClassVar[str] = "OGL-UK-2.0"
    seeAlso: ClassVar[List[str]] = ['http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/']
    isOsiApproved: ClassVar[bool] = False

class LicenseOglUk3_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OGL-UK-3.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OGL-UK-3.0.json"
    referenceNumber: ClassVar[int] = 273
    longName: ClassVar[str] = "Open Government Licence v3.0"
    licenseId: ClassVar[str] = "OGL-UK-3.0"
    seeAlso: ClassVar[List[str]] = ['http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/']
    isOsiApproved: ClassVar[bool] = False

class LicenseOgtsl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OGTSL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OGTSL.json"
    referenceNumber: ClassVar[int] = 374
    longName: ClassVar[str] = "Open Group Test Suite License"
    licenseId: ClassVar[str] = "OGTSL"
    seeAlso: ClassVar[List[str]] = ['http://www.opengroup.org/testing/downloads/The_Open_Group_TSL.txt', 'https://opensource.org/licenses/OGTSL']
    isOsiApproved: ClassVar[bool] = True

class LicenseOldap1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OLDAP-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OLDAP-1.1.json"
    referenceNumber: ClassVar[int] = 301
    longName: ClassVar[str] = "Open LDAP Public License v1.1"
    licenseId: ClassVar[str] = "OLDAP-1.1"
    seeAlso: ClassVar[List[str]] = ['http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=806557a5ad59804ef3a44d5abfbe91d706b0791f']
    isOsiApproved: ClassVar[bool] = False

class LicenseOldap1_2(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OLDAP-1.2.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OLDAP-1.2.json"
    referenceNumber: ClassVar[int] = 60
    longName: ClassVar[str] = "Open LDAP Public License v1.2"
    licenseId: ClassVar[str] = "OLDAP-1.2"
    seeAlso: ClassVar[List[str]] = ['http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=42b0383c50c299977b5893ee695cf4e486fb0dc7']
    isOsiApproved: ClassVar[bool] = False

class LicenseOldap1_3(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OLDAP-1.3.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OLDAP-1.3.json"
    referenceNumber: ClassVar[int] = 330
    longName: ClassVar[str] = "Open LDAP Public License v1.3"
    licenseId: ClassVar[str] = "OLDAP-1.3"
    seeAlso: ClassVar[List[str]] = ['http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=e5f8117f0ce088d0bd7a8e18ddf37eaa40eb09b1']
    isOsiApproved: ClassVar[bool] = False

class LicenseOldap1_4(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OLDAP-1.4.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OLDAP-1.4.json"
    referenceNumber: ClassVar[int] = 294
    longName: ClassVar[str] = "Open LDAP Public License v1.4"
    licenseId: ClassVar[str] = "OLDAP-1.4"
    seeAlso: ClassVar[List[str]] = ['http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=c9f95c2f3f2ffb5e0ae55fe7388af75547660941']
    isOsiApproved: ClassVar[bool] = False

class LicenseOldap2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.0.json"
    referenceNumber: ClassVar[int] = 497
    longName: ClassVar[str] = "Open LDAP Public License v2.0 (or possibly 2.0A and 2.0B)"
    licenseId: ClassVar[str] = "OLDAP-2.0"
    seeAlso: ClassVar[List[str]] = ['http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=cbf50f4e1185a21abd4c0a54d3f4341fe28f36ea']
    isOsiApproved: ClassVar[bool] = False

class LicenseOldap2_0_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.0.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.0.1.json"
    referenceNumber: ClassVar[int] = 242
    longName: ClassVar[str] = "Open LDAP Public License v2.0.1"
    licenseId: ClassVar[str] = "OLDAP-2.0.1"
    seeAlso: ClassVar[List[str]] = ['http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=b6d68acd14e51ca3aab4428bf26522aa74873f0e']
    isOsiApproved: ClassVar[bool] = False

class LicenseOldap2_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.1.json"
    referenceNumber: ClassVar[int] = 534
    longName: ClassVar[str] = "Open LDAP Public License v2.1"
    licenseId: ClassVar[str] = "OLDAP-2.1"
    seeAlso: ClassVar[List[str]] = ['http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=b0d176738e96a0d3b9f85cb51e140a86f21be715']
    isOsiApproved: ClassVar[bool] = False

class LicenseOldap2_2(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.2.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.2.json"
    referenceNumber: ClassVar[int] = 482
    longName: ClassVar[str] = "Open LDAP Public License v2.2"
    licenseId: ClassVar[str] = "OLDAP-2.2"
    seeAlso: ClassVar[List[str]] = ['http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=470b0c18ec67621c85881b2733057fecf4a1acc3']
    isOsiApproved: ClassVar[bool] = False

class LicenseOldap2_2_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.2.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.2.1.json"
    referenceNumber: ClassVar[int] = 332
    longName: ClassVar[str] = "Open LDAP Public License v2.2.1"
    licenseId: ClassVar[str] = "OLDAP-2.2.1"
    seeAlso: ClassVar[List[str]] = ['http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=4bc786f34b50aa301be6f5600f58a980070f481e']
    isOsiApproved: ClassVar[bool] = False

class LicenseOldap2_2_2(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.2.2.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.2.2.json"
    referenceNumber: ClassVar[int] = 239
    longName: ClassVar[str] = "Open LDAP Public License 2.2.2"
    licenseId: ClassVar[str] = "OLDAP-2.2.2"
    seeAlso: ClassVar[List[str]] = ['http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=df2cc1e21eb7c160695f5b7cffd6296c151ba188']
    isOsiApproved: ClassVar[bool] = False

class LicenseOldap2_3(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.3.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.3.json"
    referenceNumber: ClassVar[int] = 597
    longName: ClassVar[str] = "Open LDAP Public License v2.3"
    licenseId: ClassVar[str] = "OLDAP-2.3"
    seeAlso: ClassVar[List[str]] = ['http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=d32cf54a32d581ab475d23c810b0a7fbaf8d63c3']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseOldap2_4(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.4.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.4.json"
    referenceNumber: ClassVar[int] = 34
    longName: ClassVar[str] = "Open LDAP Public License v2.4"
    licenseId: ClassVar[str] = "OLDAP-2.4"
    seeAlso: ClassVar[List[str]] = ['http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=cd1284c4a91a8a380d904eee68d1583f989ed386']
    isOsiApproved: ClassVar[bool] = False

class LicenseOldap2_5(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.5.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.5.json"
    referenceNumber: ClassVar[int] = 599
    longName: ClassVar[str] = "Open LDAP Public License v2.5"
    licenseId: ClassVar[str] = "OLDAP-2.5"
    seeAlso: ClassVar[List[str]] = ['http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=6852b9d90022e8593c98205413380536b1b5a7cf']
    isOsiApproved: ClassVar[bool] = False

class LicenseOldap2_6(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.6.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.6.json"
    referenceNumber: ClassVar[int] = 231
    longName: ClassVar[str] = "Open LDAP Public License v2.6"
    licenseId: ClassVar[str] = "OLDAP-2.6"
    seeAlso: ClassVar[List[str]] = ['http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=1cae062821881f41b73012ba816434897abf4205']
    isOsiApproved: ClassVar[bool] = False

class LicenseOldap2_7(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.7.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.7.json"
    referenceNumber: ClassVar[int] = 376
    longName: ClassVar[str] = "Open LDAP Public License v2.7"
    licenseId: ClassVar[str] = "OLDAP-2.7"
    seeAlso: ClassVar[List[str]] = ['http://www.openldap.org/devel/gitweb.cgi?p=openldap.git;a=blob;f=LICENSE;hb=47c2415c1df81556eeb39be6cad458ef87c534a2']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseOldap2_8(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.8.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OLDAP-2.8.json"
    referenceNumber: ClassVar[int] = 512
    longName: ClassVar[str] = "Open LDAP Public License v2.8"
    licenseId: ClassVar[str] = "OLDAP-2.8"
    seeAlso: ClassVar[List[str]] = ['http://www.openldap.org/software/release/license.html']
    isOsiApproved: ClassVar[bool] = True

class LicenseOlfl1_3(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OLFL-1.3.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OLFL-1.3.json"
    referenceNumber: ClassVar[int] = 99
    longName: ClassVar[str] = "Open Logistics Foundation License Version 1.3"
    licenseId: ClassVar[str] = "OLFL-1.3"
    seeAlso: ClassVar[List[str]] = ['https://openlogisticsfoundation.org/licenses/', 'https://opensource.org/license/olfl-1-3/']
    isOsiApproved: ClassVar[bool] = True

class LicenseOml(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OML.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OML.json"
    referenceNumber: ClassVar[int] = 279
    longName: ClassVar[str] = "Open Market License"
    licenseId: ClassVar[str] = "OML"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Open_Market_License']
    isOsiApproved: ClassVar[bool] = False

class LicenseOpenpbs2_3(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OpenPBS-2.3.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OpenPBS-2.3.json"
    referenceNumber: ClassVar[int] = 490
    longName: ClassVar[str] = "OpenPBS v2.3 Software License"
    licenseId: ClassVar[str] = "OpenPBS-2.3"
    seeAlso: ClassVar[List[str]] = ['https://github.com/adaptivecomputing/torque/blob/master/PBS_License.txt', 'https://www.mcs.anl.gov/research/projects/openpbs/PBS_License.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseOpenssl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OpenSSL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OpenSSL.json"
    referenceNumber: ClassVar[int] = 78
    longName: ClassVar[str] = "OpenSSL License"
    licenseId: ClassVar[str] = "OpenSSL"
    seeAlso: ClassVar[List[str]] = ['http://www.openssl.org/source/license.html']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseOpl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OPL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OPL-1.0.json"
    referenceNumber: ClassVar[int] = 415
    longName: ClassVar[str] = "Open Public License v1.0"
    licenseId: ClassVar[str] = "OPL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://old.koalateam.com/jackaroo/OPL_1_0.TXT', 'https://fedoraproject.org/wiki/Licensing/Open_Public_License']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = False

class LicenseOplUk3_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OPL-UK-3.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OPL-UK-3.0.json"
    referenceNumber: ClassVar[int] = 174
    longName: ClassVar[str] = "United    Kingdom Open Parliament Licence v3.0"
    licenseId: ClassVar[str] = "OPL-UK-3.0"
    seeAlso: ClassVar[List[str]] = ['https://www.parliament.uk/site-information/copyright-parliament/open-parliament-licence/']
    isOsiApproved: ClassVar[bool] = False

class LicenseOpubl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OPUBL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OPUBL-1.0.json"
    referenceNumber: ClassVar[int] = 109
    longName: ClassVar[str] = "Open Publication License v1.0"
    licenseId: ClassVar[str] = "OPUBL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://opencontent.org/openpub/', 'https://www.debian.org/opl', 'https://www.ctan.org/license/opl']
    isOsiApproved: ClassVar[bool] = False

class LicenseOsetPl2_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OSET-PL-2.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OSET-PL-2.1.json"
    referenceNumber: ClassVar[int] = 483
    longName: ClassVar[str] = "OSET Public License version 2.1"
    licenseId: ClassVar[str] = "OSET-PL-2.1"
    seeAlso: ClassVar[List[str]] = ['http://www.osetfoundation.org/public-license', 'https://opensource.org/licenses/OPL-2.1']
    isOsiApproved: ClassVar[bool] = True

class LicenseOsl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OSL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OSL-1.0.json"
    referenceNumber: ClassVar[int] = 222
    longName: ClassVar[str] = "Open Software License 1.0"
    licenseId: ClassVar[str] = "OSL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/OSL-1.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseOsl1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OSL-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OSL-1.1.json"
    referenceNumber: ClassVar[int] = 275
    longName: ClassVar[str] = "Open Software License 1.1"
    licenseId: ClassVar[str] = "OSL-1.1"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/OSL1.1']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseOsl2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OSL-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OSL-2.0.json"
    referenceNumber: ClassVar[int] = 262
    longName: ClassVar[str] = "Open Software License 2.0"
    licenseId: ClassVar[str] = "OSL-2.0"
    seeAlso: ClassVar[List[str]] = ['http://web.archive.org/web/20041020171434/http://www.rosenlaw.com/osl2.0.html']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseOsl2_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OSL-2.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OSL-2.1.json"
    referenceNumber: ClassVar[int] = 46
    longName: ClassVar[str] = "Open Software License 2.1"
    licenseId: ClassVar[str] = "OSL-2.1"
    seeAlso: ClassVar[List[str]] = ['http://web.archive.org/web/20050212003940/http://www.rosenlaw.com/osl21.htm', 'https://opensource.org/licenses/OSL-2.1']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseOsl3_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/OSL-3.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/OSL-3.0.json"
    referenceNumber: ClassVar[int] = 56
    longName: ClassVar[str] = "Open Software License 3.0"
    licenseId: ClassVar[str] = "OSL-3.0"
    seeAlso: ClassVar[List[str]] = ['https://web.archive.org/web/20120101081418/http://rosenlaw.com:80/OSL3.0.htm', 'https://opensource.org/licenses/OSL-3.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicensePadl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/PADL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/PADL.json"
    referenceNumber: ClassVar[int] = 300
    longName: ClassVar[str] = "PADL License"
    licenseId: ClassVar[str] = "PADL"
    seeAlso: ClassVar[List[str]] = ['https://git.openldap.org/openldap/openldap/-/blob/master/libraries/libldap/os-local.c?ref_type=heads#L19-23']
    isOsiApproved: ClassVar[bool] = False

class LicenseParity6_0_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Parity-6.0.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Parity-6.0.0.json"
    referenceNumber: ClassVar[int] = 579
    longName: ClassVar[str] = "The Parity Public License 6.0.0"
    licenseId: ClassVar[str] = "Parity-6.0.0"
    seeAlso: ClassVar[List[str]] = ['https://paritylicense.com/versions/6.0.0.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseParity7_0_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Parity-7.0.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Parity-7.0.0.json"
    referenceNumber: ClassVar[int] = 521
    longName: ClassVar[str] = "The Parity Public License 7.0.0"
    licenseId: ClassVar[str] = "Parity-7.0.0"
    seeAlso: ClassVar[List[str]] = ['https://paritylicense.com/versions/7.0.0.html']
    isOsiApproved: ClassVar[bool] = False

class LicensePddl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/PDDL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/PDDL-1.0.json"
    referenceNumber: ClassVar[int] = 378
    longName: ClassVar[str] = "Open Data Commons Public Domain Dedication & License 1.0"
    licenseId: ClassVar[str] = "PDDL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://opendatacommons.org/licenses/pddl/1.0/', 'https://opendatacommons.org/licenses/pddl/']
    isOsiApproved: ClassVar[bool] = False

class LicensePhp3_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/PHP-3.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/PHP-3.0.json"
    referenceNumber: ClassVar[int] = 224
    longName: ClassVar[str] = "PHP License v3.0"
    licenseId: ClassVar[str] = "PHP-3.0"
    seeAlso: ClassVar[List[str]] = ['http://www.php.net/license/3_0.txt', 'https://opensource.org/licenses/PHP-3.0']
    isOsiApproved: ClassVar[bool] = True

class LicensePhp3_01(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/PHP-3.01.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/PHP-3.01.json"
    referenceNumber: ClassVar[int] = 35
    longName: ClassVar[str] = "PHP License v3.01"
    licenseId: ClassVar[str] = "PHP-3.01"
    seeAlso: ClassVar[List[str]] = ['http://www.php.net/license/3_01.txt']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicensePixar(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Pixar.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Pixar.json"
    referenceNumber: ClassVar[int] = 177
    longName: ClassVar[str] = "Pixar License"
    licenseId: ClassVar[str] = "Pixar"
    seeAlso: ClassVar[List[str]] = ['https://github.com/PixarAnimationStudios/OpenSubdiv/raw/v3_5_0/LICENSE.txt', 'https://graphics.pixar.com/opensubdiv/docs/license.html', 'https://github.com/PixarAnimationStudios/OpenSubdiv/blob/v3_5_0/opensubdiv/version.cpp#L2-L22']
    isOsiApproved: ClassVar[bool] = False

class LicensePlexus(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Plexus.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Plexus.json"
    referenceNumber: ClassVar[int] = 63
    longName: ClassVar[str] = "Plexus Classworlds License"
    licenseId: ClassVar[str] = "Plexus"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Plexus_Classworlds_License']
    isOsiApproved: ClassVar[bool] = False

class LicensePnmstitch(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/pnmstitch.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/pnmstitch.json"
    referenceNumber: ClassVar[int] = 105
    longName: ClassVar[str] = "pnmstitch License"
    licenseId: ClassVar[str] = "pnmstitch"
    seeAlso: ClassVar[List[str]] = ['https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/editor/pnmstitch.c#l2']
    isOsiApproved: ClassVar[bool] = False

class LicensePolyformNoncommercial1_0_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/PolyForm-Noncommercial-1.0.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/PolyForm-Noncommercial-1.0.0.json"
    referenceNumber: ClassVar[int] = 6
    longName: ClassVar[str] = "PolyForm Noncommercial License 1.0.0"
    licenseId: ClassVar[str] = "PolyForm-Noncommercial-1.0.0"
    seeAlso: ClassVar[List[str]] = ['https://polyformproject.org/licenses/noncommercial/1.0.0']
    isOsiApproved: ClassVar[bool] = False

class LicensePolyformSmallBusiness1_0_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/PolyForm-Small-Business-1.0.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/PolyForm-Small-Business-1.0.0.json"
    referenceNumber: ClassVar[int] = 341
    longName: ClassVar[str] = "PolyForm Small Business License 1.0.0"
    licenseId: ClassVar[str] = "PolyForm-Small-Business-1.0.0"
    seeAlso: ClassVar[List[str]] = ['https://polyformproject.org/licenses/small-business/1.0.0']
    isOsiApproved: ClassVar[bool] = False

class LicensePostgresql(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/PostgreSQL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/PostgreSQL.json"
    referenceNumber: ClassVar[int] = 325
    longName: ClassVar[str] = "PostgreSQL License"
    licenseId: ClassVar[str] = "PostgreSQL"
    seeAlso: ClassVar[List[str]] = ['http://www.postgresql.org/about/licence', 'https://opensource.org/licenses/PostgreSQL']
    isOsiApproved: ClassVar[bool] = True

class LicensePsf2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/PSF-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/PSF-2.0.json"
    referenceNumber: ClassVar[int] = 282
    longName: ClassVar[str] = "Python Software Foundation License 2.0"
    licenseId: ClassVar[str] = "PSF-2.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/Python-2.0']
    isOsiApproved: ClassVar[bool] = False

class LicensePsfrag(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/psfrag.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/psfrag.json"
    referenceNumber: ClassVar[int] = 194
    longName: ClassVar[str] = "psfrag License"
    licenseId: ClassVar[str] = "psfrag"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/psfrag']
    isOsiApproved: ClassVar[bool] = False

class LicensePsutils(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/psutils.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/psutils.json"
    referenceNumber: ClassVar[int] = 489
    longName: ClassVar[str] = "psutils License"
    licenseId: ClassVar[str] = "psutils"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/psutils']
    isOsiApproved: ClassVar[bool] = False

class LicensePython2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Python-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Python-2.0.json"
    referenceNumber: ClassVar[int] = 480
    longName: ClassVar[str] = "Python License 2.0"
    licenseId: ClassVar[str] = "Python-2.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/Python-2.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicensePython2_0_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Python-2.0.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Python-2.0.1.json"
    referenceNumber: ClassVar[int] = 151
    longName: ClassVar[str] = "Python License 2.0.1"
    licenseId: ClassVar[str] = "Python-2.0.1"
    seeAlso: ClassVar[List[str]] = ['https://www.python.org/download/releases/2.0.1/license/', 'https://docs.python.org/3/license.html', 'https://github.com/python/cpython/blob/main/LICENSE']
    isOsiApproved: ClassVar[bool] = False

class LicensePythonLdap(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/python-ldap.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/python-ldap.json"
    referenceNumber: ClassVar[int] = 348
    longName: ClassVar[str] = "Python ldap License"
    licenseId: ClassVar[str] = "python-ldap"
    seeAlso: ClassVar[List[str]] = ['https://github.com/zdohnal/hplip/blob/master/base/ldif.py', 'https://sourceforge.net/projects/hplip/files/hplip/3.23.5/hplip-3.23.5.tar.gz/download']
    isOsiApproved: ClassVar[bool] = False

class LicenseQhull(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Qhull.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Qhull.json"
    referenceNumber: ClassVar[int] = 291
    longName: ClassVar[str] = "Qhull License"
    licenseId: ClassVar[str] = "Qhull"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Qhull']
    isOsiApproved: ClassVar[bool] = False

class LicenseQpl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/QPL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/QPL-1.0.json"
    referenceNumber: ClassVar[int] = 509
    longName: ClassVar[str] = "Q Public License 1.0"
    licenseId: ClassVar[str] = "QPL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://doc.qt.nokia.com/3.3/license.html', 'https://opensource.org/licenses/QPL-1.0', 'https://doc.qt.io/archives/3.3/license.html']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseQpl1_0Inria2004(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/QPL-1.0-INRIA-2004.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/QPL-1.0-INRIA-2004.json"
    referenceNumber: ClassVar[int] = 356
    longName: ClassVar[str] = "Q Public License 1.0 - INRIA 2004 variant"
    licenseId: ClassVar[str] = "QPL-1.0-INRIA-2004"
    seeAlso: ClassVar[List[str]] = ['https://github.com/maranget/hevea/blob/master/LICENSE']
    isOsiApproved: ClassVar[bool] = False

class LicenseRdisc(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Rdisc.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Rdisc.json"
    referenceNumber: ClassVar[int] = 585
    longName: ClassVar[str] = "Rdisc License"
    licenseId: ClassVar[str] = "Rdisc"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Rdisc_License']
    isOsiApproved: ClassVar[bool] = False

class LicenseRhecos1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/RHeCos-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/RHeCos-1.1.json"
    referenceNumber: ClassVar[int] = 587
    longName: ClassVar[str] = "Red Hat eCos Public License v1.1"
    licenseId: ClassVar[str] = "RHeCos-1.1"
    seeAlso: ClassVar[List[str]] = ['http://ecos.sourceware.org/old-license.html']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = False

class LicenseRpl1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/RPL-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/RPL-1.1.json"
    referenceNumber: ClassVar[int] = 4
    longName: ClassVar[str] = "Reciprocal Public License 1.1"
    licenseId: ClassVar[str] = "RPL-1.1"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/RPL-1.1']
    isOsiApproved: ClassVar[bool] = True

class LicenseRpl1_5(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/RPL-1.5.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/RPL-1.5.json"
    referenceNumber: ClassVar[int] = 346
    longName: ClassVar[str] = "Reciprocal Public License 1.5"
    licenseId: ClassVar[str] = "RPL-1.5"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/RPL-1.5']
    isOsiApproved: ClassVar[bool] = True

class LicenseRpsl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/RPSL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/RPSL-1.0.json"
    referenceNumber: ClassVar[int] = 469
    longName: ClassVar[str] = "RealNetworks Public Source License v1.0"
    licenseId: ClassVar[str] = "RPSL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://helixcommunity.org/content/rpsl', 'https://opensource.org/licenses/RPSL-1.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseRsaMd(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/RSA-MD.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/RSA-MD.json"
    referenceNumber: ClassVar[int] = 576
    longName: ClassVar[str] = "RSA Message-Digest License"
    licenseId: ClassVar[str] = "RSA-MD"
    seeAlso: ClassVar[List[str]] = ['http://www.faqs.org/rfcs/rfc1321.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseRscpl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/RSCPL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/RSCPL.json"
    referenceNumber: ClassVar[int] = 314
    longName: ClassVar[str] = "Ricoh Source Code Public License"
    licenseId: ClassVar[str] = "RSCPL"
    seeAlso: ClassVar[List[str]] = ['http://wayback.archive.org/web/20060715140826/http://www.risource.org/RPL/RPL-1.0A.shtml', 'https://opensource.org/licenses/RSCPL']
    isOsiApproved: ClassVar[bool] = True

class LicenseRuby(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Ruby.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Ruby.json"
    referenceNumber: ClassVar[int] = 227
    longName: ClassVar[str] = "Ruby License"
    licenseId: ClassVar[str] = "Ruby"
    seeAlso: ClassVar[List[str]] = ['https://www.ruby-lang.org/en/about/license.txt']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseSaxPd(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SAX-PD.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SAX-PD.json"
    referenceNumber: ClassVar[int] = 554
    longName: ClassVar[str] = "Sax Public Domain Notice"
    licenseId: ClassVar[str] = "SAX-PD"
    seeAlso: ClassVar[List[str]] = ['http://www.saxproject.org/copying.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseSaxpath(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Saxpath.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Saxpath.json"
    referenceNumber: ClassVar[int] = 27
    longName: ClassVar[str] = "Saxpath License"
    licenseId: ClassVar[str] = "Saxpath"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Saxpath_License']
    isOsiApproved: ClassVar[bool] = False

class LicenseScea(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SCEA.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SCEA.json"
    referenceNumber: ClassVar[int] = 323
    longName: ClassVar[str] = "SCEA Shared Source License"
    licenseId: ClassVar[str] = "SCEA"
    seeAlso: ClassVar[List[str]] = ['http://research.scea.com/scea_shared_source_license.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseSchemereport(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SchemeReport.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SchemeReport.json"
    referenceNumber: ClassVar[int] = 488
    longName: ClassVar[str] = "Scheme Language Report License"
    licenseId: ClassVar[str] = "SchemeReport"
    seeAlso: ClassVar[List[str]] = []
    isOsiApproved: ClassVar[bool] = False

class LicenseSendmail(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Sendmail.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Sendmail.json"
    referenceNumber: ClassVar[int] = 213
    longName: ClassVar[str] = "Sendmail License"
    licenseId: ClassVar[str] = "Sendmail"
    seeAlso: ClassVar[List[str]] = ['http://www.sendmail.com/pdfs/open_source/sendmail_license.pdf', 'https://web.archive.org/web/20160322142305/https://www.sendmail.com/pdfs/open_source/sendmail_license.pdf']
    isOsiApproved: ClassVar[bool] = False

class LicenseSendmail8_23(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Sendmail-8.23.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Sendmail-8.23.json"
    referenceNumber: ClassVar[int] = 51
    longName: ClassVar[str] = "Sendmail License 8.23"
    licenseId: ClassVar[str] = "Sendmail-8.23"
    seeAlso: ClassVar[List[str]] = ['https://www.proofpoint.com/sites/default/files/sendmail-license.pdf', 'https://web.archive.org/web/20181003101040/https://www.proofpoint.com/sites/default/files/sendmail-license.pdf']
    isOsiApproved: ClassVar[bool] = False

class LicenseSgiB1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SGI-B-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SGI-B-1.0.json"
    referenceNumber: ClassVar[int] = 550
    longName: ClassVar[str] = "SGI Free Software License B v1.0"
    licenseId: ClassVar[str] = "SGI-B-1.0"
    seeAlso: ClassVar[List[str]] = ['http://oss.sgi.com/projects/FreeB/SGIFreeSWLicB.1.0.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseSgiB1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SGI-B-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SGI-B-1.1.json"
    referenceNumber: ClassVar[int] = 375
    longName: ClassVar[str] = "SGI Free Software License B v1.1"
    licenseId: ClassVar[str] = "SGI-B-1.1"
    seeAlso: ClassVar[List[str]] = ['http://oss.sgi.com/projects/FreeB/']
    isOsiApproved: ClassVar[bool] = False

class LicenseSgiB2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SGI-B-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SGI-B-2.0.json"
    referenceNumber: ClassVar[int] = 102
    longName: ClassVar[str] = "SGI Free Software License B v2.0"
    licenseId: ClassVar[str] = "SGI-B-2.0"
    seeAlso: ClassVar[List[str]] = ['http://oss.sgi.com/projects/FreeB/SGIFreeSWLicB.2.0.pdf']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseSgiOpengl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SGI-OpenGL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SGI-OpenGL.json"
    referenceNumber: ClassVar[int] = 93
    longName: ClassVar[str] = "SGI OpenGL License"
    licenseId: ClassVar[str] = "SGI-OpenGL"
    seeAlso: ClassVar[List[str]] = ['https://gitlab.freedesktop.org/mesa/glw/-/blob/master/README?ref_type=heads']
    isOsiApproved: ClassVar[bool] = False

class LicenseSgp4(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SGP4.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SGP4.json"
    referenceNumber: ClassVar[int] = 246
    longName: ClassVar[str] = "SGP4 Permission Notice"
    licenseId: ClassVar[str] = "SGP4"
    seeAlso: ClassVar[List[str]] = ['https://celestrak.org/publications/AIAA/2006-6753/faq.php']
    isOsiApproved: ClassVar[bool] = False

class LicenseShl0_5(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SHL-0.5.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SHL-0.5.json"
    referenceNumber: ClassVar[int] = 219
    longName: ClassVar[str] = "Solderpad Hardware License v0.5"
    licenseId: ClassVar[str] = "SHL-0.5"
    seeAlso: ClassVar[List[str]] = ['https://solderpad.org/licenses/SHL-0.5/']
    isOsiApproved: ClassVar[bool] = False

class LicenseShl0_51(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SHL-0.51.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SHL-0.51.json"
    referenceNumber: ClassVar[int] = 477
    longName: ClassVar[str] = "Solderpad Hardware License, Version 0.51"
    licenseId: ClassVar[str] = "SHL-0.51"
    seeAlso: ClassVar[List[str]] = ['https://solderpad.org/licenses/SHL-0.51/']
    isOsiApproved: ClassVar[bool] = False

class LicenseSimpl2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SimPL-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SimPL-2.0.json"
    referenceNumber: ClassVar[int] = 505
    longName: ClassVar[str] = "Simple Public License 2.0"
    licenseId: ClassVar[str] = "SimPL-2.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/SimPL-2.0']
    isOsiApproved: ClassVar[bool] = True

class LicenseSissl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SISSL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SISSL.json"
    referenceNumber: ClassVar[int] = 170
    longName: ClassVar[str] = "Sun Industry Standards Source License v1.1"
    licenseId: ClassVar[str] = "SISSL"
    seeAlso: ClassVar[List[str]] = ['http://www.openoffice.org/licenses/sissl_license.html', 'https://opensource.org/licenses/SISSL']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseSissl1_2(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SISSL-1.2.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SISSL-1.2.json"
    referenceNumber: ClassVar[int] = 296
    longName: ClassVar[str] = "Sun Industry Standards Source License v1.2"
    licenseId: ClassVar[str] = "SISSL-1.2"
    seeAlso: ClassVar[List[str]] = ['http://gridscheduler.sourceforge.net/Gridengine_SISSL_license.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseSl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SL.json"
    referenceNumber: ClassVar[int] = 184
    longName: ClassVar[str] = "SL License"
    licenseId: ClassVar[str] = "SL"
    seeAlso: ClassVar[List[str]] = ['https://github.com/mtoyoda/sl/blob/master/LICENSE']
    isOsiApproved: ClassVar[bool] = False

class LicenseSleepycat(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Sleepycat.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Sleepycat.json"
    referenceNumber: ClassVar[int] = 506
    longName: ClassVar[str] = "Sleepycat License"
    licenseId: ClassVar[str] = "Sleepycat"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/Sleepycat']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseSmlnj(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SMLNJ.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SMLNJ.json"
    referenceNumber: ClassVar[int] = 334
    longName: ClassVar[str] = "Standard ML of New Jersey License"
    licenseId: ClassVar[str] = "SMLNJ"
    seeAlso: ClassVar[List[str]] = ['https://www.smlnj.org/license.html']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseSmppl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SMPPL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SMPPL.json"
    referenceNumber: ClassVar[int] = 535
    longName: ClassVar[str] = "Secure Messaging Protocol Public License"
    licenseId: ClassVar[str] = "SMPPL"
    seeAlso: ClassVar[List[str]] = ['https://github.com/dcblake/SMP/blob/master/Documentation/License.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseSnia(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SNIA.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SNIA.json"
    referenceNumber: ClassVar[int] = 321
    longName: ClassVar[str] = "SNIA Public License 1.1"
    licenseId: ClassVar[str] = "SNIA"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/SNIA_Public_License']
    isOsiApproved: ClassVar[bool] = False

class LicenseSnprintf(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/snprintf.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/snprintf.json"
    referenceNumber: ClassVar[int] = 578
    longName: ClassVar[str] = "snprintf License"
    licenseId: ClassVar[str] = "snprintf"
    seeAlso: ClassVar[List[str]] = ['https://github.com/openssh/openssh-portable/blob/master/openbsd-compat/bsd-snprintf.c#L2']
    isOsiApproved: ClassVar[bool] = False

class LicenseSoundex(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Soundex.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Soundex.json"
    referenceNumber: ClassVar[int] = 121
    longName: ClassVar[str] = "Soundex License"
    licenseId: ClassVar[str] = "Soundex"
    seeAlso: ClassVar[List[str]] = ['https://metacpan.org/release/RJBS/Text-Soundex-3.05/source/Soundex.pm#L3-11']
    isOsiApproved: ClassVar[bool] = False

class LicenseSpencer86(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Spencer-86.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Spencer-86.json"
    referenceNumber: ClassVar[int] = 264
    longName: ClassVar[str] = "Spencer License 86"
    licenseId: ClassVar[str] = "Spencer-86"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Henry_Spencer_Reg-Ex_Library_License']
    isOsiApproved: ClassVar[bool] = False

class LicenseSpencer94(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Spencer-94.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Spencer-94.json"
    referenceNumber: ClassVar[int] = 215
    longName: ClassVar[str] = "Spencer License 94"
    licenseId: ClassVar[str] = "Spencer-94"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Henry_Spencer_Reg-Ex_Library_License', 'https://metacpan.org/release/KNOK/File-MMagic-1.30/source/COPYING#L28']
    isOsiApproved: ClassVar[bool] = False

class LicenseSpencer99(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Spencer-99.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Spencer-99.json"
    referenceNumber: ClassVar[int] = 439
    longName: ClassVar[str] = "Spencer License 99"
    licenseId: ClassVar[str] = "Spencer-99"
    seeAlso: ClassVar[List[str]] = ['http://www.opensource.apple.com/source/tcl/tcl-5/tcl/generic/regfronts.c']
    isOsiApproved: ClassVar[bool] = False

class LicenseSpl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SPL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SPL-1.0.json"
    referenceNumber: ClassVar[int] = 541
    longName: ClassVar[str] = "Sun Public License v1.0"
    licenseId: ClassVar[str] = "SPL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/SPL-1.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseSshKeyscan(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/ssh-keyscan.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/ssh-keyscan.json"
    referenceNumber: ClassVar[int] = 61
    longName: ClassVar[str] = "ssh-keyscan License"
    licenseId: ClassVar[str] = "ssh-keyscan"
    seeAlso: ClassVar[List[str]] = ['https://github.com/openssh/openssh-portable/blob/master/LICENCE#L82']
    isOsiApproved: ClassVar[bool] = False

class LicenseSshOpenssh(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SSH-OpenSSH.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SSH-OpenSSH.json"
    referenceNumber: ClassVar[int] = 444
    longName: ClassVar[str] = "SSH OpenSSH license"
    licenseId: ClassVar[str] = "SSH-OpenSSH"
    seeAlso: ClassVar[List[str]] = ['https://github.com/openssh/openssh-portable/blob/1b11ea7c58cd5c59838b5fa574cd456d6047b2d4/LICENCE#L10']
    isOsiApproved: ClassVar[bool] = False

class LicenseSshShort(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SSH-short.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SSH-short.json"
    referenceNumber: ClassVar[int] = 580
    longName: ClassVar[str] = "SSH short notice"
    licenseId: ClassVar[str] = "SSH-short"
    seeAlso: ClassVar[List[str]] = ['https://github.com/openssh/openssh-portable/blob/1b11ea7c58cd5c59838b5fa574cd456d6047b2d4/pathnames.h', 'http://web.mit.edu/kolya/.f/root/athena.mit.edu/sipb.mit.edu/project/openssh/OldFiles/src/openssh-2.9.9p2/ssh-add.1', 'https://joinup.ec.europa.eu/svn/lesoll/trunk/italc/lib/src/dsa_key.cpp']
    isOsiApproved: ClassVar[bool] = False

class LicenseSspl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SSPL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SSPL-1.0.json"
    referenceNumber: ClassVar[int] = 286
    longName: ClassVar[str] = "Server Side Public License, v 1"
    licenseId: ClassVar[str] = "SSPL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://www.mongodb.com/licensing/server-side-public-license']
    isOsiApproved: ClassVar[bool] = False

class LicenseStandardmlNj(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/StandardML-NJ.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/StandardML-NJ.json"
    referenceNumber: ClassVar[int] = 601
    longName: ClassVar[str] = "Standard ML of New Jersey License"
    licenseId: ClassVar[str] = "StandardML-NJ"
    seeAlso: ClassVar[List[str]] = ['https://www.smlnj.org/license.html']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseSugarcrm1_1_3(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SugarCRM-1.1.3.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SugarCRM-1.1.3.json"
    referenceNumber: ClassVar[int] = 3
    longName: ClassVar[str] = "SugarCRM Public License v1.1.3"
    licenseId: ClassVar[str] = "SugarCRM-1.1.3"
    seeAlso: ClassVar[List[str]] = ['http://www.sugarcrm.com/crm/SPL']
    isOsiApproved: ClassVar[bool] = False

class LicenseSunpro(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SunPro.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SunPro.json"
    referenceNumber: ClassVar[int] = 487
    longName: ClassVar[str] = "SunPro License"
    licenseId: ClassVar[str] = "SunPro"
    seeAlso: ClassVar[List[str]] = ['https://github.com/freebsd/freebsd-src/blob/main/lib/msun/src/e_acosh.c', 'https://github.com/freebsd/freebsd-src/blob/main/lib/msun/src/e_lgammal.c']
    isOsiApproved: ClassVar[bool] = False

class LicenseSwl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/SWL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/SWL.json"
    referenceNumber: ClassVar[int] = 370
    longName: ClassVar[str] = "Scheme Widget Library (SWL) Software License Agreement"
    licenseId: ClassVar[str] = "SWL"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/SWL']
    isOsiApproved: ClassVar[bool] = False

class LicenseSwrule(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/swrule.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/swrule.json"
    referenceNumber: ClassVar[int] = 393
    longName: ClassVar[str] = "swrule License"
    licenseId: ClassVar[str] = "swrule"
    seeAlso: ClassVar[List[str]] = ['https://ctan.math.utah.edu/ctan/tex-archive/macros/generic/misc/swrule.sty']
    isOsiApproved: ClassVar[bool] = False

class LicenseSymlinks(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Symlinks.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Symlinks.json"
    referenceNumber: ClassVar[int] = 318
    longName: ClassVar[str] = "Symlinks License"
    licenseId: ClassVar[str] = "Symlinks"
    seeAlso: ClassVar[List[str]] = ['https://www.mail-archive.com/debian-bugs-rc@lists.debian.org/msg11494.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseTaprOhl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/TAPR-OHL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/TAPR-OHL-1.0.json"
    referenceNumber: ClassVar[int] = 418
    longName: ClassVar[str] = "TAPR Open Hardware License v1.0"
    licenseId: ClassVar[str] = "TAPR-OHL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://www.tapr.org/OHL']
    isOsiApproved: ClassVar[bool] = False

class LicenseTcl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/TCL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/TCL.json"
    referenceNumber: ClassVar[int] = 569
    longName: ClassVar[str] = "TCL/TK License"
    licenseId: ClassVar[str] = "TCL"
    seeAlso: ClassVar[List[str]] = ['http://www.tcl.tk/software/tcltk/license.html', 'https://fedoraproject.org/wiki/Licensing/TCL']
    isOsiApproved: ClassVar[bool] = False

class LicenseTcpWrappers(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/TCP-wrappers.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/TCP-wrappers.json"
    referenceNumber: ClassVar[int] = 522
    longName: ClassVar[str] = "TCP Wrappers License"
    licenseId: ClassVar[str] = "TCP-wrappers"
    seeAlso: ClassVar[List[str]] = ['http://rc.quest.com/topics/openssh/license.php#tcpwrappers']
    isOsiApproved: ClassVar[bool] = False

class LicenseTermreadkey(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/TermReadKey.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/TermReadKey.json"
    referenceNumber: ClassVar[int] = 575
    longName: ClassVar[str] = "TermReadKey License"
    licenseId: ClassVar[str] = "TermReadKey"
    seeAlso: ClassVar[List[str]] = ['https://github.com/jonathanstowe/TermReadKey/blob/master/README#L9-L10']
    isOsiApproved: ClassVar[bool] = False

class LicenseTmate(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/TMate.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/TMate.json"
    referenceNumber: ClassVar[int] = 499
    longName: ClassVar[str] = "TMate Open Source License"
    licenseId: ClassVar[str] = "TMate"
    seeAlso: ClassVar[List[str]] = ['http://svnkit.com/license.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseTorque1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/TORQUE-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/TORQUE-1.1.json"
    referenceNumber: ClassVar[int] = 445
    longName: ClassVar[str] = "TORQUE v2.5+ Software License v1.1"
    licenseId: ClassVar[str] = "TORQUE-1.1"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/TORQUEv1.1']
    isOsiApproved: ClassVar[bool] = False

class LicenseTosl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/TOSL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/TOSL.json"
    referenceNumber: ClassVar[int] = 154
    longName: ClassVar[str] = "Trusster Open Source License"
    licenseId: ClassVar[str] = "TOSL"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/TOSL']
    isOsiApproved: ClassVar[bool] = False

class LicenseTpdl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/TPDL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/TPDL.json"
    referenceNumber: ClassVar[int] = 460
    longName: ClassVar[str] = "Time::ParseDate License"
    licenseId: ClassVar[str] = "TPDL"
    seeAlso: ClassVar[List[str]] = ['https://metacpan.org/pod/Time::ParseDate#LICENSE']
    isOsiApproved: ClassVar[bool] = False

class LicenseTpl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/TPL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/TPL-1.0.json"
    referenceNumber: ClassVar[int] = 228
    longName: ClassVar[str] = "THOR Public License 1.0"
    licenseId: ClassVar[str] = "TPL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing:ThorPublicLicense']
    isOsiApproved: ClassVar[bool] = False

class LicenseTtwl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/TTWL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/TTWL.json"
    referenceNumber: ClassVar[int] = 167
    longName: ClassVar[str] = "Text-Tabs+Wrap License"
    licenseId: ClassVar[str] = "TTWL"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/TTWL', 'https://github.com/ap/Text-Tabs/blob/master/lib.modern/Text/Tabs.pm#L148']
    isOsiApproved: ClassVar[bool] = False

class LicenseTtyp0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/TTYP0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/TTYP0.json"
    referenceNumber: ClassVar[int] = 127
    longName: ClassVar[str] = "TTYP0 License"
    licenseId: ClassVar[str] = "TTYP0"
    seeAlso: ClassVar[List[str]] = ['https://people.mpi-inf.mpg.de/~uwe/misc/uw-ttyp0/']
    isOsiApproved: ClassVar[bool] = False

class LicenseTuBerlin1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/TU-Berlin-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/TU-Berlin-1.0.json"
    referenceNumber: ClassVar[int] = 179
    longName: ClassVar[str] = "Technische Universitaet Berlin License 1.0"
    licenseId: ClassVar[str] = "TU-Berlin-1.0"
    seeAlso: ClassVar[List[str]] = ['https://github.com/swh/ladspa/blob/7bf6f3799fdba70fda297c2d8fd9f526803d9680/gsm/COPYRIGHT']
    isOsiApproved: ClassVar[bool] = False

class LicenseTuBerlin2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/TU-Berlin-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/TU-Berlin-2.0.json"
    referenceNumber: ClassVar[int] = 536
    longName: ClassVar[str] = "Technische Universitaet Berlin License 2.0"
    licenseId: ClassVar[str] = "TU-Berlin-2.0"
    seeAlso: ClassVar[List[str]] = ['https://github.com/CorsixTH/deps/blob/fd339a9f526d1d9c9f01ccf39e438a015da50035/licences/libgsm.txt']
    isOsiApproved: ClassVar[bool] = False

class LicenseUcar(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/UCAR.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/UCAR.json"
    referenceNumber: ClassVar[int] = 513
    longName: ClassVar[str] = "UCAR License"
    licenseId: ClassVar[str] = "UCAR"
    seeAlso: ClassVar[List[str]] = ['https://github.com/Unidata/UDUNITS-2/blob/master/COPYRIGHT']
    isOsiApproved: ClassVar[bool] = False

class LicenseUcl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/UCL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/UCL-1.0.json"
    referenceNumber: ClassVar[int] = 267
    longName: ClassVar[str] = "Upstream Compatibility License v1.0"
    licenseId: ClassVar[str] = "UCL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/UCL-1.0']
    isOsiApproved: ClassVar[bool] = True

class LicenseUlem(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/ulem.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/ulem.json"
    referenceNumber: ClassVar[int] = 237
    longName: ClassVar[str] = "ulem License"
    licenseId: ClassVar[str] = "ulem"
    seeAlso: ClassVar[List[str]] = ['https://mirrors.ctan.org/macros/latex/contrib/ulem/README']
    isOsiApproved: ClassVar[bool] = False

class LicenseUnicodeDfs2015(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Unicode-DFS-2015.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Unicode-DFS-2015.json"
    referenceNumber: ClassVar[int] = 383
    longName: ClassVar[str] = "Unicode License Agreement - Data Files and Software (2015)"
    licenseId: ClassVar[str] = "Unicode-DFS-2015"
    seeAlso: ClassVar[List[str]] = ['https://web.archive.org/web/20151224134844/http://unicode.org/copyright.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseUnicodeDfs2016(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Unicode-DFS-2016.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Unicode-DFS-2016.json"
    referenceNumber: ClassVar[int] = 8
    longName: ClassVar[str] = "Unicode License Agreement - Data Files and Software (2016)"
    licenseId: ClassVar[str] = "Unicode-DFS-2016"
    seeAlso: ClassVar[List[str]] = ['https://www.unicode.org/license.txt', 'http://web.archive.org/web/20160823201924/http://www.unicode.org/copyright.html#License', 'http://www.unicode.org/copyright.html']
    isOsiApproved: ClassVar[bool] = True

class LicenseUnicodeTou(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Unicode-TOU.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Unicode-TOU.json"
    referenceNumber: ClassVar[int] = 26
    longName: ClassVar[str] = "Unicode Terms of Use"
    licenseId: ClassVar[str] = "Unicode-TOU"
    seeAlso: ClassVar[List[str]] = ['http://web.archive.org/web/20140704074106/http://www.unicode.org/copyright.html', 'http://www.unicode.org/copyright.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseUnixcrypt(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/UnixCrypt.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/UnixCrypt.json"
    referenceNumber: ClassVar[int] = 241
    longName: ClassVar[str] = "UnixCrypt License"
    licenseId: ClassVar[str] = "UnixCrypt"
    seeAlso: ClassVar[List[str]] = ['https://foss.heptapod.net/python-libs/passlib/-/blob/branch/stable/LICENSE#L70', 'https://opensource.apple.com/source/JBoss/JBoss-737/jboss-all/jetty/src/main/org/mortbay/util/UnixCrypt.java.auto.html', 'https://archive.eclipse.org/jetty/8.0.1.v20110908/xref/org/eclipse/jetty/http/security/UnixCrypt.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseUnlicense(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Unlicense.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Unlicense.json"
    referenceNumber: ClassVar[int] = 113
    longName: ClassVar[str] = "The Unlicense"
    licenseId: ClassVar[str] = "Unlicense"
    seeAlso: ClassVar[List[str]] = ['https://unlicense.org/']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseUpl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/UPL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/UPL-1.0.json"
    referenceNumber: ClassVar[int] = 181
    longName: ClassVar[str] = "Universal Permissive License v1.0"
    licenseId: ClassVar[str] = "UPL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/UPL']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseUrtRle(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/URT-RLE.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/URT-RLE.json"
    referenceNumber: ClassVar[int] = 306
    longName: ClassVar[str] = "Utah Raster Toolkit Run Length Encoded License"
    licenseId: ClassVar[str] = "URT-RLE"
    seeAlso: ClassVar[List[str]] = ['https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/converter/other/pnmtorle.c', 'https://sourceforge.net/p/netpbm/code/HEAD/tree/super_stable/converter/other/rletopnm.c']
    isOsiApproved: ClassVar[bool] = False

class LicenseVim(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Vim.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Vim.json"
    referenceNumber: ClassVar[int] = 10
    longName: ClassVar[str] = "Vim License"
    licenseId: ClassVar[str] = "Vim"
    seeAlso: ClassVar[List[str]] = ['http://vimdoc.sourceforge.net/htmldoc/uganda.html']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseVostrom(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/VOSTROM.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/VOSTROM.json"
    referenceNumber: ClassVar[int] = 169
    longName: ClassVar[str] = "VOSTROM Public License for Open Source"
    licenseId: ClassVar[str] = "VOSTROM"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/VOSTROM']
    isOsiApproved: ClassVar[bool] = False

class LicenseVsl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/VSL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/VSL-1.0.json"
    referenceNumber: ClassVar[int] = 531
    longName: ClassVar[str] = "Vovida Software License v1.0"
    licenseId: ClassVar[str] = "VSL-1.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/VSL-1.0']
    isOsiApproved: ClassVar[bool] = True

class LicenseW3c(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/W3C.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/W3C.json"
    referenceNumber: ClassVar[int] = 381
    longName: ClassVar[str] = "W3C Software Notice and License (2002-12-31)"
    licenseId: ClassVar[str] = "W3C"
    seeAlso: ClassVar[List[str]] = ['http://www.w3.org/Consortium/Legal/2002/copyright-software-20021231.html', 'https://opensource.org/licenses/W3C']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseW3c19980720(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/W3C-19980720.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/W3C-19980720.json"
    referenceNumber: ClassVar[int] = 394
    longName: ClassVar[str] = "W3C Software Notice and License (1998-07-20)"
    licenseId: ClassVar[str] = "W3C-19980720"
    seeAlso: ClassVar[List[str]] = ['http://www.w3.org/Consortium/Legal/copyright-software-19980720.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseW3c20150513(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/W3C-20150513.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/W3C-20150513.json"
    referenceNumber: ClassVar[int] = 406
    longName: ClassVar[str] = "W3C Software Notice and Document License (2015-05-13)"
    licenseId: ClassVar[str] = "W3C-20150513"
    seeAlso: ClassVar[List[str]] = ['https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document']
    isOsiApproved: ClassVar[bool] = False

class LicenseW3m(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/w3m.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/w3m.json"
    referenceNumber: ClassVar[int] = 514
    longName: ClassVar[str] = "w3m License"
    licenseId: ClassVar[str] = "w3m"
    seeAlso: ClassVar[List[str]] = ['https://github.com/tats/w3m/blob/master/COPYING']
    isOsiApproved: ClassVar[bool] = False

class LicenseWatcom1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Watcom-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Watcom-1.0.json"
    referenceNumber: ClassVar[int] = 421
    longName: ClassVar[str] = "Sybase Open Watcom Public License 1.0"
    licenseId: ClassVar[str] = "Watcom-1.0"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/Watcom-1.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = False

class LicenseWidgetWorkshop(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Widget-Workshop.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Widget-Workshop.json"
    referenceNumber: ClassVar[int] = 452
    longName: ClassVar[str] = "Widget Workshop License"
    licenseId: ClassVar[str] = "Widget-Workshop"
    seeAlso: ClassVar[List[str]] = ['https://github.com/novnc/noVNC/blob/master/core/crypto/des.js#L24']
    isOsiApproved: ClassVar[bool] = False

class LicenseWsuipa(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Wsuipa.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Wsuipa.json"
    referenceNumber: ClassVar[int] = 390
    longName: ClassVar[str] = "Wsuipa License"
    licenseId: ClassVar[str] = "Wsuipa"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Wsuipa']
    isOsiApproved: ClassVar[bool] = False

class LicenseWtfpl(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/WTFPL.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/WTFPL.json"
    referenceNumber: ClassVar[int] = 199
    longName: ClassVar[str] = "Do What The F*ck You Want To Public License"
    licenseId: ClassVar[str] = "WTFPL"
    seeAlso: ClassVar[List[str]] = ['http://www.wtfpl.net/about/', 'http://sam.zoy.org/wtfpl/COPYING']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseWxwindows(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/wxWindows.html"
    isDeprecatedLicenseId: ClassVar[bool] = True
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/wxWindows.json"
    referenceNumber: ClassVar[int] = 182
    longName: ClassVar[str] = "wxWindows Library License"
    licenseId: ClassVar[str] = "wxWindows"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/WXwindows']
    isOsiApproved: ClassVar[bool] = True

class LicenseX11(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/X11.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/X11.json"
    referenceNumber: ClassVar[int] = 539
    longName: ClassVar[str] = "X11 License"
    licenseId: ClassVar[str] = "X11"
    seeAlso: ClassVar[List[str]] = ['http://www.xfree86.org/3.3.6/COPYRIGHT2.html#3']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseX11DistributeModificationsVariant(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/X11-distribute-modifications-variant.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/X11-distribute-modifications-variant.json"
    referenceNumber: ClassVar[int] = 158
    longName: ClassVar[str] = "X11 License Distribution Modification Variant"
    licenseId: ClassVar[str] = "X11-distribute-modifications-variant"
    seeAlso: ClassVar[List[str]] = ['https://github.com/mirror/ncurses/blob/master/COPYING']
    isOsiApproved: ClassVar[bool] = False

class LicenseXdebug1_03(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Xdebug-1.03.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Xdebug-1.03.json"
    referenceNumber: ClassVar[int] = 265
    longName: ClassVar[str] = "Xdebug License v 1.03"
    licenseId: ClassVar[str] = "Xdebug-1.03"
    seeAlso: ClassVar[List[str]] = ['https://github.com/xdebug/xdebug/blob/master/LICENSE']
    isOsiApproved: ClassVar[bool] = False

class LicenseXerox(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Xerox.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Xerox.json"
    referenceNumber: ClassVar[int] = 591
    longName: ClassVar[str] = "Xerox License"
    licenseId: ClassVar[str] = "Xerox"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Xerox']
    isOsiApproved: ClassVar[bool] = False

class LicenseXfig(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Xfig.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Xfig.json"
    referenceNumber: ClassVar[int] = 384
    longName: ClassVar[str] = "Xfig License"
    licenseId: ClassVar[str] = "Xfig"
    seeAlso: ClassVar[List[str]] = ['https://github.com/Distrotech/transfig/blob/master/transfig/transfig.c', 'https://fedoraproject.org/wiki/Licensing:MIT#Xfig_Variant', 'https://sourceforge.net/p/mcj/xfig/ci/master/tree/src/Makefile.am']
    isOsiApproved: ClassVar[bool] = False

class LicenseXfree861_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/XFree86-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/XFree86-1.1.json"
    referenceNumber: ClassVar[int] = 577
    longName: ClassVar[str] = "XFree86 License 1.1"
    licenseId: ClassVar[str] = "XFree86-1.1"
    seeAlso: ClassVar[List[str]] = ['http://www.xfree86.org/current/LICENSE4.html']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseXinetd(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/xinetd.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/xinetd.json"
    referenceNumber: ClassVar[int] = 385
    longName: ClassVar[str] = "xinetd License"
    licenseId: ClassVar[str] = "xinetd"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Xinetd_License']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseXlock(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/xlock.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/xlock.json"
    referenceNumber: ClassVar[int] = 19
    longName: ClassVar[str] = "xlock License"
    licenseId: ClassVar[str] = "xlock"
    seeAlso: ClassVar[List[str]] = ['https://fossies.org/linux/tiff/contrib/ras/ras2tif.c']
    isOsiApproved: ClassVar[bool] = False

class LicenseXnet(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Xnet.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Xnet.json"
    referenceNumber: ClassVar[int] = 165
    longName: ClassVar[str] = "X.Net License"
    licenseId: ClassVar[str] = "Xnet"
    seeAlso: ClassVar[List[str]] = ['https://opensource.org/licenses/Xnet']
    isOsiApproved: ClassVar[bool] = True

class LicenseXpp(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/xpp.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/xpp.json"
    referenceNumber: ClassVar[int] = 530
    longName: ClassVar[str] = "XPP License"
    licenseId: ClassVar[str] = "xpp"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/xpp']
    isOsiApproved: ClassVar[bool] = False

class LicenseXskat(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/XSkat.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/XSkat.json"
    referenceNumber: ClassVar[int] = 52
    longName: ClassVar[str] = "XSkat License"
    licenseId: ClassVar[str] = "XSkat"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/XSkat_License']
    isOsiApproved: ClassVar[bool] = False

class LicenseYpl1_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/YPL-1.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/YPL-1.0.json"
    referenceNumber: ClassVar[int] = 567
    longName: ClassVar[str] = "Yahoo! Public License v1.0"
    licenseId: ClassVar[str] = "YPL-1.0"
    seeAlso: ClassVar[List[str]] = ['http://www.zimbra.com/license/yahoo_public_license_1.0.html']
    isOsiApproved: ClassVar[bool] = False

class LicenseYpl1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/YPL-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/YPL-1.1.json"
    referenceNumber: ClassVar[int] = 141
    longName: ClassVar[str] = "Yahoo! Public License v1.1"
    licenseId: ClassVar[str] = "YPL-1.1"
    seeAlso: ClassVar[List[str]] = ['http://www.zimbra.com/license/yahoo_public_license_1.1.html']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseZed(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Zed.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Zed.json"
    referenceNumber: ClassVar[int] = 259
    longName: ClassVar[str] = "Zed License"
    licenseId: ClassVar[str] = "Zed"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/Zed']
    isOsiApproved: ClassVar[bool] = False

class LicenseZeeff(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Zeeff.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Zeeff.json"
    referenceNumber: ClassVar[int] = 76
    longName: ClassVar[str] = "Zeeff License"
    licenseId: ClassVar[str] = "Zeeff"
    seeAlso: ClassVar[List[str]] = ['ftp://ftp.tin.org/pub/news/utils/newsx/newsx-1.6.tar.gz']
    isOsiApproved: ClassVar[bool] = False

class LicenseZend2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Zend-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Zend-2.0.json"
    referenceNumber: ClassVar[int] = 32
    longName: ClassVar[str] = "Zend License v2.0"
    licenseId: ClassVar[str] = "Zend-2.0"
    seeAlso: ClassVar[List[str]] = ['https://web.archive.org/web/20130517195954/http://www.zend.com/license/2_00.txt']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseZimbra1_3(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Zimbra-1.3.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Zimbra-1.3.json"
    referenceNumber: ClassVar[int] = 589
    longName: ClassVar[str] = "Zimbra Public License v1.3"
    licenseId: ClassVar[str] = "Zimbra-1.3"
    seeAlso: ClassVar[List[str]] = ['http://web.archive.org/web/20100302225219/http://www.zimbra.com/license/zimbra-public-license-1-3.html']
    isOsiApproved: ClassVar[bool] = False
    isFsfLibre: ClassVar[bool] = True

class LicenseZimbra1_4(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Zimbra-1.4.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Zimbra-1.4.json"
    referenceNumber: ClassVar[int] = 380
    longName: ClassVar[str] = "Zimbra Public License v1.4"
    licenseId: ClassVar[str] = "Zimbra-1.4"
    seeAlso: ClassVar[List[str]] = ['http://www.zimbra.com/legal/zimbra-public-license-1-4']
    isOsiApproved: ClassVar[bool] = False

class LicenseZlib(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/Zlib.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/Zlib.json"
    referenceNumber: ClassVar[int] = 172
    longName: ClassVar[str] = "zlib License"
    licenseId: ClassVar[str] = "Zlib"
    seeAlso: ClassVar[List[str]] = ['http://www.zlib.net/zlib_license.html', 'https://opensource.org/licenses/Zlib']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseZlibAcknowledgement(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/zlib-acknowledgement.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/zlib-acknowledgement.json"
    referenceNumber: ClassVar[int] = 311
    longName: ClassVar[str] = "zlib/libpng License with Acknowledgement"
    licenseId: ClassVar[str] = "zlib-acknowledgement"
    seeAlso: ClassVar[List[str]] = ['https://fedoraproject.org/wiki/Licensing/ZlibWithAcknowledgement']
    isOsiApproved: ClassVar[bool] = False

class LicenseZpl1_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/ZPL-1.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/ZPL-1.1.json"
    referenceNumber: ClassVar[int] = 91
    longName: ClassVar[str] = "Zope Public License 1.1"
    licenseId: ClassVar[str] = "ZPL-1.1"
    seeAlso: ClassVar[List[str]] = ['http://old.zope.org/Resources/License/ZPL-1.1']
    isOsiApproved: ClassVar[bool] = False

class LicenseZpl2_0(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/ZPL-2.0.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/ZPL-2.0.json"
    referenceNumber: ClassVar[int] = 478
    longName: ClassVar[str] = "Zope Public License 2.0"
    licenseId: ClassVar[str] = "ZPL-2.0"
    seeAlso: ClassVar[List[str]] = ['http://old.zope.org/Resources/License/ZPL-2.0', 'https://opensource.org/licenses/ZPL-2.0']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True

class LicenseZpl2_1(PredefinedLicense):
    reference: ClassVar[str] = "https://spdx.org/licenses/ZPL-2.1.html"
    isDeprecatedLicenseId: ClassVar[bool] = False
    detailsUrl: ClassVar[str] = "https://spdx.org/licenses/ZPL-2.1.json"
    referenceNumber: ClassVar[int] = 399
    longName: ClassVar[str] = "Zope Public License 2.1"
    licenseId: ClassVar[str] = "ZPL-2.1"
    seeAlso: ClassVar[List[str]] = ['http://old.zope.org/Resources/ZPL/']
    isOsiApproved: ClassVar[bool] = True
    isFsfLibre: ClassVar[bool] = True
