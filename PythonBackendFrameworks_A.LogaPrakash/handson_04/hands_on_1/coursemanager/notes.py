# ==============================================================================
# HANDS-ON 1: Web Framework Foundations & Django Project Setup
# File: notes.py
# Description: Conceptual notes covering Web Framework Fundamentals,
#              Request-Response Cycle, WSGI vs ASGI, MVC vs MVT, and
#              Django Projects vs Apps.
# ==============================================================================

"""
1. THE JOURNEY OF A GET /api/courses/ REQUEST THROUGH A DJANGO APPLICATION
------------------------------------------------------------------------------
The journey of an HTTP GET /api/courses/ request from the browser to the response
follows this step-by-step lifecycle:

  [Browser / Client]
         │
         ▼  (1) HTTP GET Request /api/courses/
   [Web Server] (e.g., Nginx, Gunicorn, runserver)
         │
         ▼  (2) WSGI / ASGI Handler (Entrypoint: wsgi.py / asgi.py)
  ┌──────┼────────────────────────────────────────┐
  │      ▼  (3) Request Middleware                │
  │  [Middleware Chain] (e.g., Security, Session) │
  │      │                                        │
  │      ▼  (4) URL Routing (urls.py)             │
  │  [URL Router] maps '/api/courses/' to view    │
  │      │                                        │
  │      ▼  (5) View Execution (views.py)         │
  │  [Django View] receives request, executes     │
  │      │                                        │
  │      ├─► [Django Model] (models.py)           │
  │      │   Queries DB (SQL: SELECT * FROM ...)  │
  │      │   and returns QuerySet/Data to View    │
  │      │                                        │
  │      ├─► [Django Template] (optional)         │
  │      │   Renders HTML context if needed       │
  │      │                                        │
  │      ▼  (6) Response Generation               │
  │  [Django View] constructs & returns Response  │
  │      │                                        │
  │      ▼  (7) Response Middleware               │
  │  [Middleware Chain] (e.g., Session, Common)   │
  └──────┼────────────────────────────────────────┘
         │
         ▼  (8) HTTP Response (JSON/HTML/etc.)
   [Web Server]
         │
         ▼  (9) Rendered page/data
  [Browser / Client]


2. MIDDLEWARE IN THE REQUEST-RESPONSE CYCLE
------------------------------------------------------------------------------
* What is Middleware?
  Middleware is a framework of hooks into Django's request/response processing.
  It is a light, low-level "plugin" system for globally altering Django's input or output.
  It acts as a gatekeeper sitting between the Web Server (WSGI/ASGI) and the URL Router/Views.

* Where does it sit?
  It sits directly between the incoming request interface (WSGI/ASGI) and the URL router,
  and conversely, between the view output (Response) and the outgoing server interface.

* Two Built-in Django Middleware Classes:
  1. django.middleware.security.SecurityMiddleware:
     - Purpose: Provides several security enhancements for the request/response cycle.
     - Role: It enforces HTTPS redirects, sets the 'X-Content-Type-Options: nosniff' header
             to prevent mime-sniffing, manages HTTP Strict Transport Security (HSTS),
             and configures the X-XSS-Protection header.
  2. django.contrib.sessions.middleware.SessionMiddleware:
     - Purpose: Manages sessions across HTTP requests.
     - Role: It handles reading session data from cookie-based session IDs in the request
             and serializing/saving session data back into the database or cache store
             during the response.


3. WSGI VS ASGI
------------------------------------------------------------------------------
* WSGI (Web Server Gateway Interface):
  - Nature: Synchronous.
  - Standard: PEP 3333.
  - Role: The traditional Python standard for web servers. It handles requests sequentially
          in a single-thread/blocking fashion. It is designed for standard HTTP request-response cycles.
  - Django Default: Yes, Django has historically used WSGI by default (`wsgi.py` handles this entry point).

* ASGI (Asynchronous Server Gateway Interface):
  - Nature: Asynchronous.
  - Standard: Successor to WSGI.
  - Role: Supports both synchronous and asynchronous code. It is designed to handle multiple
          protocols, including HTTP, WebSockets, gRPC, and long polling. It enables non-blocking,
          asynchronous request processing.
  - When to switch to ASGI:
    - When you need to build real-time interactive applications (e.g., WebSockets, chat rooms).
    - When you require long-running connections (e.g., Server-Sent Events, long polling).
    - When you have high-concurrency workloads that benefit from Python's async/await concurrency model.


4. MVC VS MVT PATTERNS
------------------------------------------------------------------------------
* MVC (Model-View-Controller) Pattern:
  - Model: Manages data, database schema, and core business logic.
  - View: Represents the presentation layer (what the user sees, e.g., HTML/UI).
  - Controller: Handles user input, interacts with the Model, and determines which View to render.

* MVT (Model-View-Template) Pattern in Django:
  - Model (M): Maps directly to the database tables. Defines data structure and logic.
  - View (V): Corresponds to the Controller in MVC. It contains the business logic,
              processes the requests, queries models, and determines what data to send to the template.
  - Template (T): Corresponds to the View in MVC. It is the presentation layer (HTML, CSS, template variables)
                  that defines how data should be formatted and displayed.

* MVC-to-MVT Mapping Table:
  ┌──────────────────────┬──────────────────────┬──────────────────────────────────────────┐
  │ MVC Component        │ MVT Equivalent       │ Role in Django                           │
  ├──────────────────────┼──────────────────────┼──────────────────────────────────────────┤
  │ Model (M)            │ Model (M)            │ Database tables & schema ORM definition. │
  │ View (V)             │ Template (T)         │ Presentation layer (HTML, UI, formatting)│
  │ Controller (C)       │ View (V)             │ Request processing, routing, logic.      │
  └──────────────────────┴──────────────────────┴──────────────────────────────────────────┘


5. DIFFERENCE BETWEEN A DJANGO PROJECT AND A DJANGO APP
------------------------------------------------------------------------------
* Django Project:
  - Definition: The overall, complete web application configuration.
  - Scope: A project contains the main configurations, including database settings, middleware lists,
           installed apps registries, global URL routings (`urls.py`), and WSGI/ASGI configurations.
           A project acts as the container.

* Django App:
  - Definition: A self-contained, modular sub-package designed to perform a specific function.
  - Scope: An app contains its own models, views, templates, test suites, and sub-routing (`urls.py`).
           An app can be plugged into multiple projects (e.g., `django.contrib.auth`, `django.contrib.admin`),
           and a single Django project can contain many apps.
"""

if __name__ == "__main__":
    print("Django Web Framework Foundations notes loaded.")
