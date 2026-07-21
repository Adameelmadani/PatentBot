<!-- Slide number: 1 -->

# Discoverability and Analytics

### Notes:

<!-- Slide number: 2 -->
# Progressive Enhancement
Discoverability and PWA’s

Progressive enhancement = content available to all users
JS sites are indexed by Google**
Test your site with Fetch as Google tool

**Follow these best practices

### Notes:
Ref: https://plus.google.com/+JohnMueller/posts/LT4fU7kFB8W

Progressive Enhancement
Use "feature detection" & "progressive enhancement"  techniques to make your content available to all users.
Avoid redirecting to an "unsupported browser" page.
Consider using a polyfill or other safe fallback where needed.

JS based sites
Google crawler needs to index what’s going on in your site.
People often wonder if the crawler will be able to do this for JS-based sites.
Google’s crawler will work with JS, but there are some specific practices that have to be followed - these are detailed in this post.

Test your site
There is a tool called “Fetch as Google” that enables you to test how Google crawls or renders a URL on your site.
You can use this tool to see:
 whether Googlebot can access a page on your site
 how it renders the page
and whether any page resources (such as images or scripts) are blocked to Googlebot.
This tool simulates a crawl and render execution as done in Google's normal crawling and rendering process, and is useful for debugging crawl issues on your site.

<!-- Slide number: 3 -->
# What is Google Analytics?
Data is generated from user behavior
Data is processed by Google Analytics back end
Reports are generated

### Notes:
Google Analytics is a service that collects, processes, and reports data about an application’s use patterns and performance.

Adding Google Analytics to a web application enables the collection of data like visitor traffic, user agent, user’s location, etc.

This data is sent to Google Analytics servers where it is processed. The processed data is then reported to the developer and/or application owner. These reports are accessible from the Google Analytics web interface (a dashboard) and through a reporting API.

Why use it?
Using analytics tools gives developers valuable information on their application such as:
User’s geographic location, user agent, screen resolution, and language
How long users spend on pages, how often they visit pages, and the order that pages are viewed
What times users are visiting the site and from where they arrived at the site
Google Analytics is free, relatively simple to integrate, and customizable.

<!-- Slide number: 4 -->
# Integration process overview
Create account and “property”
Paste tracking snippet
(Optional) Add custom analytics

### Notes:
The general process of integrating Google Analytics into your app it as follows:

(1) First, you must create a Google Analytics account. Each account has “properties”. These typically represent applications. (This will be covered on the next slide)

(2) Once you have created an account and property, you receive a tracking snippet for the property. This is a piece of JavaScript. You paste that JavaScript snippet into your app’s code. This is the code that sends data to Google Analytics back-end.

(3) you can also use the analytics library to create custom analytics, such as tracking specific user actions

<!-- Slide number: 5 -->
# Accounts and properties
Account:
My Company
Property #1:
iOS app

Property #2:
Android app

Property #3:
Web app

Property ID: 12345-6
Property ID: 23456-7
Property ID: 34567-8

### Notes:
Using Google Analytics requires creating a Google Analytics account.

An account has properties, that represent individual collections of data. These properties have property ID’s - also called tracking ID’s - that identify them to Google Analytics.

For example, an account might represent a company. One property in that account might represent the company’s web site, while another property might represent the company’s iOS or Android app.

If you only have one app, the simplest scenario is to create a single Google Analytics account, and add a single property to that account. That property can represent your app.

<!-- Slide number: 6 -->
# Adding analytics to your app
<script>

// [a bunch of uglified JS]
ga('create', 'UA-XXXXXXXX-Y', 'auto');
ga('send', 'pageview');

</script>

### Notes:
Once you have created your account, you get a tracking snippet that contains your tracking/property ID.

This entire script needs to be pasted into the code for every page that you want to track.

At a high level, when this script runs, it:
Creates an async script tag that downloads analytics.js, the analytics library
Defines the ga function, called the command queue
Creates a "tracker" that gathers user data
Sends this data as a pageview "hit" (HTTP request) to Google Analytics
This data is analyzed and stored in your analytics account.

This snippet provides the basic functionality of Google Analytics. In addition to the data gathered by tracker creation, the pageview event allows Google Analytics to infer what pages the user is visiting, how long they are visiting them, and in what order.

For simpler applications, this the only coding required.

NOTE: you can replace analytics.js with analytics_debug.js for console debugging. Using this version will log detailed messages to the console that breakdown each hit sent. It also logs warnings and errors for your tracking code.
---------------------------------------------------------------------------------------
This code in more detail:

Every time a page with the snippet loads, the tracking snippet script is executed and the IIFE in the script does two things
Creates another <script> tag that starts asynchronously downloading analytics.js (highlighted in green), the library that does all of the analytics work.
Initializes a global “ga” function (highlighted in yellow), called the command queue. This function allows “commands” to be scheduled and run once the analytics.js library has loaded.

The next lines add two commands to the queue. The first creates a new tracker object. Tracker objects track and store data. When the new tracker is created, the analytics library gets the user’s IP address, user agent, and other page information, and stores it in the tracker. From this info Google Analytics can extract:
User’s geographic location
User’s browser and operating system (OS)
Screen size
If Flash or Java is installed
The referring site (if available)

The second command sends a “hit”. This sends all of the tracker’s data to Google Analytics.

Sending a hit is also used to note a user interaction with your app. The user interaction is specified by the hit type, in this case a “pageview”.

Since the tracker was created with your tracking ID (same as property ID), this data is sent to your account and property.

<!-- Slide number: 7 -->
# The Google Analytics dashboard

![GA records overview.png](GoogleShape121p20.jpg)

### Notes:
The data is sent to Google Analytics back end, where it is processed into reports. These reports are available through the Google Analytics dashboard.

This can be viewed in the reporting tab of your account on the Google Analytics site.

(Shown) Shown here is the Audience Overview interface. Here you can see general information such as pageview records, bounce rate, ratio of new and returning visitor, and other statistics.

<!-- Slide number: 8 -->
# The Google Analytics dashboard (cont.)

![GA details.png](GoogleShape127p21.jpg)

### Notes:
You can also see specific information like visitors’ language, country, city, browser, operating system, service provider, screen resolution, and device. Here we are looking at users’ city.

<!-- Slide number: 9 -->
# Real-time analytics

![Ga real time small.png](GoogleShape133p22.jpg)

### Notes:
It’s also possible to view analytics information in real time. This interface allows you to see hits as the occur on your site, rather than viewing them as a past record.

There are an extensive amount of features and functionality in the Google Analytics dashboard. A wide variety of reports exist, and custom reports can be created.  A link to more resources will be supplied at the end of the slides.

(Knowing how to use analytics for improving your business or increasing revenue is a skill within itself)

Reference:
Learn about the Google Analytics dashboard in depth

<!-- Slide number: 10 -->
# Custom events
ga('send', {
  hitType: 'event',
  eventCategory: 'products',
  eventAction: 'view more',
  eventLabel: 'premium'
});
// Alternative syntax
ga('send', 'event', 'products', 'view more', 'premium');

### Notes:
Google Analytics supports custom events that allow fine grain analysis of user behavior.

This codes uses the ga command queue, which is defined in the tracking snippet. The "send" command is used to send an "event". Values associated with the event are added as parameters. These values represent the eventCategory, eventAction, and eventLabel. All of these are arbitrary, and used to organize events.

Sending these custom events allow us to deeply understand user interactions with our site.

For example, here we are sending a “view more” event. This might be used to indicate that a user has viewed an item from our site. The eventLabel tells us that it was a “premium” product.

<!-- Slide number: 11 -->
# Example: Push notifications
registration.pushManager.subscribe({
  userVisibleOnly: true
})
.then(function(pushSubscription) {
  ga('send', 'event', 'push', 'subscribe');
});

### Notes:
You can add events to fire when users subscribe or unsubscribe to push notifications, as well as when there is is an error in a subscription process. This can give you an understanding of how many users are subscribing (or unsubscribing) to your app.

Here we send a “subscribe” event letting us know that a user has subscribed to our notifications.

<!-- Slide number: 12 -->
# Analytics and service workers
The Analytics ga function requires Window
Service worker hits use the Measurement Protocol API:

POST /collect HTTP/1.1Host: www.google-analytics.comv=1&tid=UA-XXXXX-Y&cid=555&t=pageview&dp=%2Fhome

### Notes:
Much of the functionality of push notifications and other progressive web app features occur in a service worker. This is an important note for analytics because the service worker script runs on its own thread and doesn’t have access to the ga command queue object (established by the tracking snippet code), which is on the main thread and requires the Window object.

Service workers must use the Measurement protocol API instead of the command queue.

The measurement protocol API is essentially POSTing hit parameters to a Google analytics endpoint.

<!-- Slide number: 13 -->
# Measurement Protocol example
self.addEventListener('notificationclose', function(event) {
  event.waitUntil(
    fetch('https://www.google-analytics.com/collect', {
      method: 'post',
      body: 'v=1&cid=...&tid=UA-XXXXXXXX-Y&t=event&' +
            'ec=notification&ea=delay&el=serviceworker'
    });
  );
});
service-worker.js

### Notes:
In this example
Service worker listens for notification close
Sends a hit (via POST) with tracking ID, and custom event parameters, along with some other required parameters for the API.
Observe that we have used event.waitUntil to wrap an asynchronous operation. event.waitUntil extends the life of an event until the asynchronous actions inside of it have completed. This ensures that the service worker will not be terminated while waiting for an asynchronous action to complete.

Measurement protocol

<!-- Slide number: 14 -->
# What about when users are offline?
Install
$ npm install --save-dev sw-offline-google-analytics

Service worker
importScripts('path/to/offline-google-analytics-import.js');
goog.offlineGoogleAnalytics.initialize();

### Notes:
Since hits are effectively HTTP requests, they won’t be sent successfully if the user is offline.

Using service worker and IndexedDB, hits can be stored when users are offline and sent at a later time when they have reconnected.

Fortunately, the sw-offline-google-analytics npm package abstracts this process for us.

(Shown) To integrate offline analytics, install the package in your project with the npm install command. Then in the service worker script, import the offline-google-analytics-import.js library, and initialize the goog.offlineGoogleAnalytics object.

(If unfamiliar, importScripts() is a worker function that lets you import scripts.)

This adds a fetch event handler to the service worker that only listens for requests made to the Google Analytics domain, which is what occurs when a hit is sent. The handler attempts to send Google Analytics hits just like we have done so far, by network requests. If the network request fails however, the request is stored in IndexedDB. The stored hits will be resent when connectivity is restored.

Reference:
ImportScripts
Offline Google Analytics npm package
Google I/O offline example
Node package manager (npm)
IndexedDB

<!-- Slide number: 15 -->
# Analytics stored in IndexedDB

![GA idb.png](GoogleShape171p28.jpg)

### Notes:
You can test this behavior by enabling Offline mode in developer tools, and then triggering Google Analytics hits on your app.

IndexedDB will show a list of URLs that represent the unsent hit requests. (You may need to click the refresh icon inside the IndexedDB interface to see them).

If you disable Offline mode and refresh the page, you should see that the URL’s are cleared, indicating that they have been sent.

<!-- Slide number: 16 -->
# Lab Overview
Create a Google Analytics & Firebase account
Add analytics to an app
View analytics data
Add custom events to understand user behavior
Use analytics with service workers (& push notifications)
Use the Measurement Protocol API
Add offline analytics to an app

### Notes:

<!-- Slide number: 17 -->
# Resources
Resources
analytics.js
Reporting API
Google Analytics Academy
Account signup
Analytics for mobile applications
Chrome debugger extension

ImportScripts
Offline Google Analytics
IndexedDB
Measuring Critical Performance Metrics with Google Analytics
Measurement Protocol
Google I/O offline example

### Notes:

<!-- Slide number: 18 -->
# UI reference slides

### Notes:

<!-- Slide number: 19 -->
# Finding your tracking snippet & ID

![GA account create.png](GoogleShape197p32.jpg)
Select the Admin tab
Under “account”, select your account from the drop down list.
Then under “properties”, select your property from the down list.
Now choose “tracking info”, followed by “tracking code”.

### Notes:

<!-- Slide number: 20 -->
# Finding the Audience Overview interface

![GA records overview.png](GoogleShape203p33.jpg)
Select the Reporting tab

Select Audience in the side panel

Select Overview

### Notes:

<!-- Slide number: 21 -->
# Finding the Real-time Overview interface

![GA real time nav.png](GoogleShape210p34.jpg)
Select the Reporting tab

Select Real-time in the side panel

Select Overview

### Notes:

<!-- Slide number: 22 -->
# Finding the Real-time Events interface

![GA real time events.png](GoogleShape217p35.jpg)
Select the Reporting tab

Select Real-time in the side panel

Select Events

### Notes:

<!-- Slide number: 23 -->
# Finding the Events Overview interface
Select the Reporting tab

Select Behavior in the side panel

Select Events

Select Overview

![GA past events.png](GoogleShape224p36.jpg)

### Notes: