<header>

<!--
  <<< Author notes: Course header >>>
 
-->

### About

The RESCUEDog Project unites an existing database of rescued animals with a company that looks for and trains rescue dogs. Grazioso Salvare, an international rescue animal training company, has teamed up with Global Rain to find rescue dogs in the Austin, Texas area.

</header>

<!--
  <<< Author notes: Finish >>>
  Review what we learned, ask for feedback, provide next steps.
-->

### Motivation

Some dogs can be trained to find and help rescue humans or other animals. Finding these dogs is the motivation behind this project. Where better to start looking for these valuable service dogs than among the populations housed in animal shelters?


### Installation

Replicating this project will require MongoDB. This application uses a managed MongoDB Atlas cluster on the cloud, however, there are also self-managed options. Next, the MongoDB Shell must be installed locally. Note, the existing data Global Rain used was provided by regional animal shelters and in comma separated value (csv) format, a format compatible for import into MongoDB.

Python was used and for web application development and with the PyMongo driver to access the MongoDB database. PyMongo provides tools to work with MongoDB, such as MongoClient that is used to connect to MongoDB with Python. The PyMongo driver and other libraries can be downloaded from within an IDE or through PIP on the command line.

Python Libraries used include:

- pymongo.MongoClient – used to connect to MongoDB.
- bson.objectid.ObjectId – used to work with MongoDB ObjectIds.
- pprint.pprint – used for formatting cursor output.

### Importing data

The mongoimport command was used to upload the data. In this case, a csv file is uploaded to the animals collection in the AAC database.

![image](https://github.com/user-attachments/assets/02820e9d-a0ac-4e51-9b22-ce9cfa5406f6)

### Defining Users

Defining users can be accomplished via Atlas or the command line, as shown below. Once connected through mongosh (Mongo Shell) locally to a MongoDB Atlas server, user can be set up to have access to a database. 

![image](https://github.com/user-attachments/assets/f471e123-8eaf-4c03-9451-a8271b23949e)

For example, in a database named “admin”:

_admin> db.createUser({ user: ”username”, pwd: passwordPrompt(), roles:[{role: “readWrite”, db: “AAC”}]})_

gives readWrite access to the username for the AAC database. Confirm the new user in the admin database with: 

_admin> db.runCommand({connectionStatus:1})_

### Indexing
Before proceeding to use the Python module, indexes may be written that benefit frequently searched criteria. For example, a compound index containing breed and age of canines may be frequently searched. An example of a single index for “breed”, created in the MongoDB Shell is shown.

![image](https://github.com/user-attachments/assets/e79cec68-0771-4fe3-a30f-e86d5fb22168)

### Usage
The purpose of the Python module (AnimalShelter.py) is to utilize object oriented programming principles to encapsulate and keep abstract the methods used on the data. These methods code the four basic operations of persistent data storage; create, read, update, and delete (CRUD). The module also allows the defining of a MongoDB instance. With each instance being unique, the connection to MongoDB can be authenticated and pre-defined access (shown above) granted to the user. The CRUD commands in the AnimalShelter.py are shown below.

![image](https://github.com/user-attachments/assets/15da884a-6109-4ee8-959f-bc9510292701)

The AnimalShelter.py was tested with the Python script below. Two Python dictionaries, newAnimal & changes, are declared. An AnimalShelter object ,a1, is created: a1 =  AnimalShelter(). Then the CRUD methods are tested, and the output is shown below.

![image](https://github.com/user-attachments/assets/8bc877df-77d8-45b6-b094-7fe58745139b)

Tests were run on all the CRUD methods to see if exceptions were properly handled. Note, only the create() method is shown below.  An exception is properly thrown when newAnimal = None

![image](https://github.com/user-attachments/assets/ace302e2-ee5d-4592-943c-be4d1af74091)
![image](https://github.com/user-attachments/assets/bde780de-e153-4919-9fed-32bd49ea08eb)

### User Interface

The User Interface was designed with the most basic goals satisfied. The user will be able to find  candidate dogs from the database of sheltered animals by choosing the desired Rescue Type button, as shown below. Choosing a Rescue Type will filter the data to include only the dogs who meet pre-defined criteria. The criteria were provided by Grazioso Salvare and hard coded into the application.

![image](https://github.com/user-attachments/assets/93022264-2ad0-4299-b860-a3d7bdfcc2a5)
![image](https://github.com/user-attachments/assets/7bd6614e-d3de-41d8-a756-56eca361dfdc)

Screenshot 1A – Water Rescue Type (top half)

Screenshot 1A shows the resulting data table when Water Rescue Type is selected from the application user interface. Below is the bottom half of the screen (shown separately for clarity) which shows a Pie Chart and Geolocation of the candidates listed in the results. The Pie Chart should show a breakdown of the breeds listed in the results.

![image](https://github.com/user-attachments/assets/4c719589-5745-49fe-9741-9e113ae5bce7)

Screenshot 1B – Water Rescue Type (bottom half)
The following screenshots show each of the outcomes when choosing the other filtering options.

![image](https://github.com/user-attachments/assets/64d39758-a945-4500-9d6c-6a4457178082)
Screenshot 2 – Mountain or Wilderness Rescue Type

![image](https://github.com/user-attachments/assets/dea7a44f-9df9-42d4-9361-de04b84daa4e)
Screenshot 3 – Disaster or Individual Tracking Rescue Type

![image](https://github.com/user-attachments/assets/2d4ed248-753c-418f-bdcb-d41f9c41013f)
Screenshot 4 – Reset reloads the unfiltered data.

### Contact
Howard.Taylor@snhu.edu

### References

- Giamas, A. (2022). Expert Techniques to Run High-volume and Fault-tolerant Database Solutions Using MongoDB 6.x. https://web-p-ebscohost-com.ezproxy.snhu.edu/ehost/ebookviewer/ebook?sid=cd951675-8b84-44aa-b0ea-14f7f5ed640d%40redis&ppid=Page-__-171&vid=0&format=EK.

- MongoDB, Inc. (2023). Create a User. https://www.mongodb.com/docs/v6.0/tutorial/create-users/

- Dayley, B. (2015). Sams Teach Yourself NoSQL with MongoDB in 24 Hours. Pearson Education.

<footer>

<!--
  <<< Author notes: Footer >>>
  Add a link to get support, GitHub status page, code of conduct, license link.
-->

---

Get help: [Post in our discussion board](https://github.com/orgs/skills/discussions/categories/github-pages) &bull; [Review the GitHub status page](https://www.githubstatus.com/)

&copy; 2023 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

</footer>
