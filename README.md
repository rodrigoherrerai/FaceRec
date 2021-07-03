# happy_face

### Terminal install:
```diff
@ -pip install happy_face
```

### Import:

```
from happy_face.happy_face import HappyFace
```
## Introduction:
#### happy_face was built on many different amazing libraries, mainly face_recognition from Adam Geitgey, dlib and many more. I do not take any accomplishment in doing this, it is just an easy way of implementing face_recognition for people that are starting.
#### The main purpose of happy_face is to show the magic of deep learning to people that are just starting with programming.
#### It has few functions, but it is extremely easy to use, this motivates people that are just starting because in python you do not see visual results until later in the journey, this can sometimes kill the creative energy.



### Brief Explanation: 
#### You just need to create a variable, instantiate it with HappyFace and fill three params:
* known_person_path_file: is the path to the SINGLE image of the face that you want to be recognized. 
* unknown_images_path_file: here is the path to the FOLDER where you have all the other images that you want to recognize.
* known_name : The name of the known_person_path_file, this will display Found U! If left empty.

#### IMPORTANT!!! Make sure your files (folders or pictures) DO NOT START WITH A DOT --> . <---, if they do, the application will have troubles to execute, this is because sometimes there are hidden files and they start with a dot. This was taken into consideration so the application runs smoothly, just make sure that your folders and files (images) do NOT start with a dot ---> . <---

### Sample Code:
```
tiger_woods = HappyFace(known_person_path_file= '/Users/Desktop/tiger.png', 
                    unknown_images_path_file = '/Users/Desktop/unknown_pictures', 
                        known_name= 'Tiger Woods')
```

#### Functions:
* display_known_im() -- will display the known_person_path_file image
* detects_known_face() -- will detect the face of the known person
* detects_unknown_faces() -- will detect all the faces of the images provided in the unknown_images_path_file folder
* recognize_faces() -- Will recognize either the person is you (or whoever you provided) or a stranger
### Sample Code:
```
tiger_woods.display_known_im() #Will display the image

tiger_woods.detects_known_face() #Will detect the face of (in this case) Tiger Woods

tiger_woods.detects_unknown_faces() #Will detect all the faces provided of the unknown people

tiger_woods.recognize_faces() -- # Will recognize either the person is tiger woods or a stranger

```


### EXAMPLE:
<img src ="https://github.com/rodrigoherrerai/FaceRec/blob/main/images/picandfolder.png" width="450" height="300"><img src ="https://github.com/rodrigoherrerai/FaceRec/blob/main/images/inside.png">
<img src="https://github.com/rodrigoherrerai/FaceRec/blob/main/images/recognize_faces.png">

### OUTPUT:

<img src="https://github.com/rodrigoherrerai/FaceRec/blob/main/images/output1.png">
<img src="https://github.com/rodrigoherrerai/FaceRec/blob/main/images/output2.png">
<img src = "https://github.com/rodrigoherrerai/FaceRec/blob/main/images/output.png">










