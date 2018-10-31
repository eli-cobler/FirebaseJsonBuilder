# FirebaseJsonBuilder

Command line tool that builds a json tree for Firebase Database import.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

Things you need to have installed for the software to work.

```
python 3.6+
```

### Installing

Clone the repo to your local machine

## Running the app

Run the app 

```
python firebaseJsonBuilder.py
```

Answer the prompts

```
What do you want to name this json file? locations
```

```
What do you want to name your parent tree? Locations
```

Make sure to seperate the childs with a space. See [locations.json](locations.json) for example
```
What child(s) do you want to add for this parent? Google Facebook
```

Same for the keys. Seperate with a space between each. Do this for each child you entered.
```
Does the child "Google" have a key(s)? google.com green 9ms
```

Once done you should see ```Json file created.``` Congradulations you are done!


## Built With

* [Python](https://www.python.org)


