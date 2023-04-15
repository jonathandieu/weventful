# weventful
Weventful is a site where students can access official university events. It's a full-stack web application built using TypeScript / React in the frontend, and a Python FastAPI backend, storing information in a Postgres SQL relational database.

# Features:
## Events:
- Events will have a name, a category, a description, time, date, location, contact info (like a phone number or email address)
## Users:
- Any user may register to obtain a user ID and a password.
- Users can be one of three levels: *Super Admin*, *Admin*, or *Student*.
  - Super Admins can create and maintain a University Profile
  - Admins can create a RSO Profile
  - Students use the application to look up information about the various events.
- When logged in, a student can view all public events, private events specific to their university, and any events of Registered Student Orgnizations where they are a member.
- Students can also rate and comment on events that they access to in order to provide feedback or to create a discussion.
