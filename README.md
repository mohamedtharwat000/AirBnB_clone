## 0x00. AirBnB clone - The console

#### Welcome to the AirBnB clone project!
##### First step: Write a command interpreter to manage your AirBnB objects.



###### Each task is linked and will help you to:
- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine


###### What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object



![Photo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230809%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230809T190853Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a82bf4f7a408ca352df1955c238cc36fb88c2eb218d780564a7e755247ef0bdf)
