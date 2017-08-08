students = [
    {'first_name' : 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# for val in students:
#     print val['first_name'], val['last_name']


users = {
    'Students': [
        {'first_name' : 'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

    # for key, data in users.items():
    #     count = 0
    #     print 'KEY', key
    #     # print 'DATA', data

    #     for value in data:
    #         secNum = (len(value["first_name"]) + len(value["last_name"]))
    #         print value["first_name"], value["last_name"], '-', secNum
def names(users):
    for key, values in users.items():
        print key #prints 'Students' 'Instructors'
        for val in range(len(values)):   
            fn = values[val]["first_name"]
            ln = values[val]["last_name"]
            #secNum variable gives total length of character names      
            secNum = (len(values[val]["first_name"]) + len(values[val]["last_name"]))
            # print val + 1, '-', values[val]["first_name"], values[val]["last_name"], '-', secNum
            print '{} - {} {} - {}'.format(val+1, fn, ln, secNum)
names(users)