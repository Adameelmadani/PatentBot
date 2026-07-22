# Discoverability and Analytics

# Progressive Enhancement

# Discoverability and PWA’s

- Progressive enhancement = content available to all users
- JS sites are indexed by Google**
- Test your site with Fetch as Google tool

**Follow these best practices

# What is Google Analytics?

Data is generated from user behavior

Data is processed by Google Analytics back end

Reports are generated

# Integration process overview	

1. Create account and “property”
2. Paste tracking snippet
3. (Optional) Add custom analytics

# Accounts and properties

Property #1: 

iOS app

Property ID: 12345-6

Account: 

My Company

Property #2: 

Android app

Property ID: 23456-7

Property #3: 

Web app

Property ID: 34567-8

# Adding analytics to your app

&lt;script&gt;

// [a bunch of uglified JS]

ga('create', 'UA-XXXXXXXX-Y', 'auto');

ga('send', 'pageview');

&lt;/script&gt;

# The Google Analytics dashboard

<!-- image -->

# The Google Analytics dashboard (cont.)

<!-- image -->

# Real-time analytics

<!-- image -->

# Custom events

ga('send', {

  hitType: 'event',

  eventCategory: 'products',

  eventAction: 'view more',

  eventLabel: 'premium'

});

// Alternative syntax

ga('send', 'event', 'products', 'view more', 'premium');

# Example: Push notifications

registration.pushManager.subscribe({

  userVisibleOnly: true

})

.then(function(pushSubscription) {

  ga('send', 'event', 'push', 'subscribe'); 

});

# Analytics and service workers

- The Analytics ga function requires Window
- Service worker hits use the Measurement Protocol API:

POST /collect HTTP/1.1 Host: www.google-analytics.com  v=1&amp;tid=UA-XXXXX-Y&amp;cid=555&amp;t=pageview&amp;dp=%2Fhome

# Measurement Protocol example

self.addEventListener('notificationclose', function(event) {

  event.waitUntil(

    fetch('https://www.google-analytics.com/collect', {

      method: 'post',

      body: 'v=1&amp;cid=...&amp;tid=UA-XXXXXXXX-Y&amp;t=event&amp;' +

            'ec=notification&amp;ea=delay&amp;el=serviceworker'

    });

  );

});

service-worker.js

# What about when users are offline?

Install

$ npm install --save-dev sw-offline-google-analytics

Service worker

importScripts('path/to/offline-google-analytics-import.js');

goog.offlineGoogleAnalytics.initialize();

# Analytics stored in IndexedDB

<!-- image -->

# Lab Overview

- Create a Google Analytics &amp; Firebase account
- Add analytics to an app
- View analytics data
- Add custom events to understand user behavior
- Use analytics with service workers (&amp; push notifications)
- Use the Measurement Protocol API
- Add offline analytics to an app

# Resources

- analytics.js 
- Reporting API
- Google Analytics Academy 
- Account signup
- Analytics for mobile applications
- Chrome debugger extension

- ImportScripts
- Offline Google Analytics 
- IndexedDB
- Measuring Critical Performance Metrics with Google Analytics
- Measurement Protocol
- Google I/O offline example

# Resources

# UI reference slides

# Finding your tracking snippet &amp; ID

1. Select the Admin tab 
2. Under “account”, select your account from the drop down list. 
3. Then under “properties”, select your property from the down list. 
4. Now choose “tracking info”, followed by “tracking code”. 

<!-- image -->

# Finding the Audience Overview interface

<!-- image -->

1. Select the Reporting tab

1. Select Audience in the side panel

1. Select Overview

# Finding the Real-time Overview interface

<!-- image -->

1. Select the Reporting tab

1. Select Real-time in the side panel

1. Select Overview

# Finding the Real-time Events interface

<!-- image -->

1. Select the Reporting tab

1. Select Real-time in the side panel

1. Select Events

# Finding the Events Overview interface

<!-- image -->

1. Select the Reporting tab

1. Select Behavior in the side panel

1. Select Events 

1. Select Overview 