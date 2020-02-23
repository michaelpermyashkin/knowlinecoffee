# KnowLineCoffee 
A Django progressive web application developed for Shippensburg University where I currently attend. The application allows users to view and update the current lines at 2 coffee shops on campus. 

## Purpose
I wanted to experiment with web development and challenge myself by building a product for hundred of users. This required learning a new framework, understanding UI and UX concepts and deployment principles to deliver the product. 

## The Result
[View Flyer](KLC-flyer.pdf)
[Visit Site](https://www.knowlinecoffee.com)

### User Interface
The main view displays Starbucks and Dunkin Donuts side by side showing the latest updates for both location. The view shows how long ago the latest update was provided. The application also averages updates within the last 2 minutes.

Users have the option to update the line when on the home screen. The updating page shows the latest update to the user and provides a scroll bar where they can input a new number to reflect the current line length.

### Progressive Web Application
The application implements PWA functionality. When users navigate to the site, they can install the app onto their homescreen which will create a native-like experience when interacting from the homescreen.

### Authentication
Users must create an account before making any updates to the application. Authentication is handled securely with a Django library and all credentials are stored in a MySQL database. 

### GeoLocation
The application requests the users location before determining if they are eligible to make an update. This requires users to be within a 50 foot radius of either location. Users within a valid radius are then able to provide an update to indicate the current line length.
