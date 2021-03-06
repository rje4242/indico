// This file is part of Indico.
// Copyright (C) 2002 - 2020 CERN
//
// Indico is free software; you can redistribute it and/or
// modify it under the terms of the MIT License; see the
// LICENSE file for more details.

import React from 'react';
import ReactDOM from 'react-dom';

import {Translate} from 'indico/react/i18n';

import ICSCalendarLink from './ICSCalendarLink';

document.addEventListener('DOMContentLoaded', () => {
  const userId = document.querySelector('body').dataset.userId;
  ReactDOM.render(
    <ICSCalendarLink
      endpoint="users.export_dashboard_ics"
      urlParams={{user_id: userId}}
      options={[
        {key: 'events', text: Translate.string('Events at hand'), queryParams: {linked: 'true'}},
        {
          key: 'categories',
          text: Translate.string('Categories'),
          queryParams: {categories: 'true'},
        },
        {key: 'everything', text: Translate.string('Everything'), queryParams: {}},
      ]}
    />,
    document.querySelector('#dashboard-calendar-link')
  );
});
