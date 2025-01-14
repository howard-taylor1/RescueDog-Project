<header>

<!--
  <<< Author notes: Course header >>>
  Include a 1280×640 image, course title in sentence case, and a concise description in emphasis.
  In your repository settings: enable template repository, add your 1280×640 social image, auto delete head branches.
  Add your open source license, GitHub uses MIT license.
-->

## RESCUEDog Project

The RESCUEDog Project unites an existing database of rescued animals with a company that looks for and trains rescue dogs. Grazioso Salvare, an innovative international rescue animal training company, has teamed up with Global Rain to find rescue dogs in the Austin, Texas area.

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

### Importing the data

The mongoimport command was used to upload the data. In this case, a csv file is uploaded to the animals collection in the AAC database.

![image](https://github.com/user-attachments/assets/02820e9d-a0ac-4e51-9b22-ce9cfa5406f6)

### Defining Users

Defining users can be accomplished via Atlas or the command line, as shown below. Once connected through mongosh (Mongo Shell) locally to a MongoDB Atlas server, user can be set up to have access to a database. 

![image](https://github.com/user-attachments/assets/f471e123-8eaf-4c03-9451-a8271b23949e)


<footer>

<!--
  <<< Author notes: Footer >>>
  Add a link to get support, GitHub status page, code of conduct, license link.
-->

---

Get help: [Post in our discussion board](https://github.com/orgs/skills/discussions/categories/github-pages) &bull; [Review the GitHub status page](https://www.githubstatus.com/)

&copy; 2023 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

</footer>
