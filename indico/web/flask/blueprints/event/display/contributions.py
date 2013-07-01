# -*- coding: utf-8 -*-
##
##
## This file is part of Indico.
## Copyright (C) 2002 - 2013 European Organization for Nuclear Research (CERN).
##
## Indico is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 3 of the
## License, or (at your option) any later version.
##
## Indico is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Indico. If not, see <http://www.gnu.org/licenses/>.

from MaKaC.webinterface.rh import conferenceDisplay, contribDisplay, subContribDisplay, authorDisplay
from indico.web.flask.util import rh_as_view
from indico.web.flask.blueprints.event.display import event


# Contribution list
event.add_url_rule('/contributions', 'contributionListDisplay', rh_as_view(conferenceDisplay.RHContributionList))
event.add_url_rule('/contributions.pdf', 'contributionListDisplay-contributionsToPDF',
                   rh_as_view(conferenceDisplay.RHContributionListToPDF), methods=('POST',))

# Display contribution
event.add_url_rule('/contribution/<contribId>', 'contributionDisplay', rh_as_view(contribDisplay.RHContributionDisplay))
event.add_url_rule('/contribution/<contribId>.ics', 'contributionDisplay-ical',
                   rh_as_view(contribDisplay.RHContributionToiCal))
event.add_url_rule('/contribution/<contribId>.marc.xml', 'contributionDisplay-marcxml',
                   rh_as_view(contribDisplay.RHContributionToMarcXML))
event.add_url_rule('/contribution/<contribId>.xml', 'contributionDisplay-xml',
                   rh_as_view(contribDisplay.RHContributionToXML))
event.add_url_rule('/contribution/<contribId>.pdf', 'contributionDisplay-pdf',
                   rh_as_view(contribDisplay.RHContributionToPDF))
event.add_url_rule('/contribution/<contribId>/<subContId>', 'subContributionDisplay',
                   rh_as_view(subContribDisplay.RHSubContributionDisplay))
event.add_url_rule('/contribution/<contribId>/<subContId>.marc.xml', 'subContributionDisplay-marcxml',
                   rh_as_view(subContribDisplay.RHSubContributionToMarcXML))

# Display contribution within a session
event.add_url_rule('/session/<sessionId>/contribution/<contribId>', 'contributionDisplay',
                   rh_as_view(contribDisplay.RHContributionDisplay))
event.add_url_rule('/session/<sessionId>/contribution/<contribId>.ics', 'contributionDisplay-ical',
                   rh_as_view(contribDisplay.RHContributionToiCal))
event.add_url_rule('/session/<sessionId>/contribution/<contribId>.marc.xml', 'contributionDisplay-marcxml',
                   rh_as_view(contribDisplay.RHContributionToMarcXML))
event.add_url_rule('/session/<sessionId>/contribution/<contribId>.xml', 'contributionDisplay-xml',
                   rh_as_view(contribDisplay.RHContributionToXML))
event.add_url_rule('/session/<sessionId>/contribution/<contribId>.pdf', 'contributionDisplay-pdf',
                   rh_as_view(contribDisplay.RHContributionToPDF))
event.add_url_rule('/session/<sessionId>/contribution/<contribId>/<subContId>', 'subContributionDisplay',
                   rh_as_view(subContribDisplay.RHSubContributionDisplay))
event.add_url_rule('/session/<sessionId>/contribution/<contribId>/<subContId>.marc.xml',
                   'subContributionDisplay-marcxml', rh_as_view(subContribDisplay.RHSubContributionToMarcXML))

# Authors/Speakers
event.add_url_rule('/authors', 'confAuthorIndex', rh_as_view(conferenceDisplay.RHAuthorIndex))
event.add_url_rule('/contribution/<contribId>/author/<authorId>', 'contribAuthorDisplay',
                   rh_as_view(authorDisplay.RHAuthorDisplay))
event.add_url_rule('/speakers', 'confSpeakerIndex', rh_as_view(conferenceDisplay.RHSpeakerIndex))
