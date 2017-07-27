var user = {
  'Students': [
    {firstName:'Michael', lastName: 'Jordan'},
    {firstName: 'John', lastName: 'Rosales'},
    {firstName: 'Mark', lastName: 'Guillen'},
    {firstName: 'KB', lastName: 'Tonel'}
  ],
  'Instructors': [
    {firstName:'Michael', lastName: 'Choi'},
    {firstName: 'Martin', lastName: 'Puryear'}
    ]
  };
console.log('Students');
  for (var i = 0; i < user.Students.length; i++) {
    var fullname = user.Students[i].firstName + user.Students[i].lastName;
   console.log(`${i+1} - ${user.Students[i].firstName} ${user.Students[i].lastName} - ${fullname.length}`);
  }
console.log('Instructors');
  for (var i = 0; i < user.Instructors.length; i++) {
    var fullname = user.Instructors[i].firstName + user.Instructors[i].lastName;
   console.log(`${i+1} - ${user.Instructors[i].firstName} ${user.Instructors[i].lastName} - ${fullname.length}`);
  }