#Vedanth M
MyProgLangDict = {
    #You can add more programming languages and their founders to this dictionary below
    "python"        : "Guido van Rossum",
    "java"          : "James Gosling",
    "javascript"    : "Brendan Eich",
    "swift"         : "Chris Lattner",
    "C"             : "Dennis Ritchie",
    "C#"            : "Andrers Hejlsberg",
    "C++"           : "Bjarne Stroustrup",
    "R"             : "Ross lhaka and Robert Gentleman",
    "ruby"          : "Yukihiro Matsumoto",
    "SQL"           : "Donald D and Raymond F Boyce",
    "PHP"           : "Rasmus Lerdorf",
    "kotlin"        : "JetBrains Company",
    "groovy"        : "James Strachan",
    "fortan"        : "John Backus",
    "cobol"         : "Grace Hopper",
    "pascal"        : "Niklaus Wirth",
    "rust"          : "Graydone Hoare",
    "scala"         : "Martin Odersky"
} 

print("The list of programming languages in my Dictionary are: \n",list(MyProgLangDict.keys()))

a = input("Enter the name of a Programming Language:\n")
print("The Founder of this programming language is:\n",MyProgLangDict.get(a))
