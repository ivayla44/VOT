# VOT - simple flask application for creating and viewing playlists by uploading mp3 files from your machine #

**Used technologies:**
----------

**Python** - Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis. Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn't specialized for any specific problems.

----------

Because it is one of the leading programming languages, there is no scarcity of frameworks for Python. Different frameworks have their own set of advantages and issues. By automating the implementation of redundant tasks, frameworks cut development time and enable developers to focus greatly on application logic rather than routine elements.

----------

**Flask** - Flask is a web framework, it’s a Python module that lets you develop web applications easily. It’s has a small and easy-to-extend core. It is classified as a microframework because it does not require particular tools or libraries. Flask allows the developers to build a solid web application foundation from where it is possible to use any kind of extensions required.

-----------

**HTTP requests** - One of flask's advantages is that it handles http requests - The request context keeps track of the request-level data during a request. Rather than passing the request object to each function that runs during a request, the request and session proxies are accessed instead. When the Flask application handles a request, it creates a Request object based on the environment it received from the WSGI server. Because a worker (thread, process, depending on the server) handles only one request at a time, the request data can be considered global to that worker during that request. Flask automatically pushes a request context when handling a request. View functions, error handlers, and other functions that run during a request will have access to the request proxy, which points to the request object for the current request.

-----------

**HTML and CSS** - HTML (Hypertext Markup Language) and CSS (Cascading Style Sheets) are two fundamental technologies used for creating and designing web pages. They work together to define the structure, content, and presentation of a webpage. HTML is the standard markup language used for creating the structure and content of web pages. It consists of a set of tags that are used to define different elements on a webpage. CSS is a style sheet language used for describing the presentation and appearance of HTML elements. It provides a way to control the layout, colors, fonts, and other visual aspects of a webpage. Overall, HTML and CSS are essential building blocks for web development, allowing developers to create attractive, well-structured, and user-friendly web pages.

-----------

**Azure** - Azure Serverless Application is a cloud computing model provided by Microsoft Azure that allows developers to build and deploy applications without the need to manage the underlying infrastructure. It enables developers to focus on writing code and implementing business logic, while Azure takes care of scaling, maintenance, and availability. The benefits of Azure applications are:
- scalability -Azure automatically scales the serverless infrastructure based on the workload, ensuring that your application can handle varying levels of traffic and demand without manual intervention
- cost-efficiency - with serverless, you only pay for the actual execution time and resources consumed by your application, eliminating the need to provision and pay for idle resources; (and Azure offers free credit for school accounts)
- simplified management - Azure takes care of managing and monitoring the infrastructure, including updates, security patches, and availability, allowing developers to focus on writing code

-----------

**The application itself** is a very simple web application - it consists of a page where the user can upload .mp3 files from there machine and create "playlists" as well as view all of their created playlists.

-----------
