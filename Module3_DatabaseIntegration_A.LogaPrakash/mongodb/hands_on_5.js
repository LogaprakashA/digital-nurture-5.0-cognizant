use college_nosql
switched to db college_nosql
db["feedback"].find()
use college_nosql
already on db college_nosql
db.feedback.insertMany([
{
student_id:1,
course_code:"CS101",
semester:"2022-ODD",
rating:5,
comments:"Excellent teaching",
tags:["challenging","well-structured","good-examples"],
submitted_at:new Date(),
attachments:[{filename:"notes.pdf",size_kb:240}]
},
{
student_id:2,
course_code:"CS101",
semester:"2022-ODD",
rating:4,
comments:"Very good course",
tags:["challenging","good-examples"],
submitted_at:new Date(),
attachments:[{filename:"lab.pdf",size_kb:120}]
},
{
student_id:3,
course_code:"CS101",
semester:"2022-ODD",
rating:3,
comments:"Average experience",
tags:["well-structured"],
submitted_at:new Date()
},
{
student_id:4,
course_code:"CS102",
semester:"2022-ODD",
rating:2,
comments:"Needs improvement",
tags:["difficult"],
submitted_at:new Date(),
attachments:[{filename:"report.pdf",size_kb:300}]
},
{
student_id:5,
course_code:"CS102",
semester:"2022-ODD",
rating:1,
comments:"Poor explanation",
tags:["confusing"],
submitted_at:new Date()
},
{
student_id:6,
course_code:"CS103",
semester:"2022-ODD",
rating:5,
comments:"Excellent",
tags:["good-examples"],
submitted_at:new Date()
},
{
student_id:7,
course_code:"CS104",
semester:"2021-EVEN",
rating:4,
comments:"Good",
tags:["interactive"],
submitted_at:new Date()
},
{
student_id:8,
course_code:"CS105",
semester:"2022-ODD",
rating:5,
comments:"Outstanding",
tags:["challenging"],
submitted_at:new Date()
},
{
student_id:9,
course_code:"CS106",
semester:"2022-ODD",
rating:3,
comments:"Decent",
tags:["well-structured"],
submitted_at:new Date()
},
{
student_id:10,
course_code:"CS107",
semester:"2022-ODD",
rating:4,
comments:"Helpful",
tags:["good-examples"],
submitted_at:new Date()
}
])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6a324d90412a847f96907121'),
    '1': ObjectId('6a324d90412a847f96907122'),
    '2': ObjectId('6a324d90412a847f96907123'),
    '3': ObjectId('6a324d90412a847f96907124'),
    '4': ObjectId('6a324d90412a847f96907125'),
    '5': ObjectId('6a324d90412a847f96907126'),
    '6': ObjectId('6a324d90412a847f96907127'),
    '7': ObjectId('6a324d90412a847f96907128'),
    '8': ObjectId('6a324d90412a847f96907129'),
    '9': ObjectId('6a324d90412a847f9690712a')
  }
}
db.feedback.countDocuments()
10
db.feedback.find({rating:5})
{
  _id: ObjectId('6a324d90412a847f96907121'),
  student_id: 1,
  course_code: 'CS101',
  semester: '2022-ODD',
  rating: 5,
  comments: 'Excellent teaching',
  tags: [
    'challenging',
    'well-structured',
    'good-examples'
  ],
  submitted_at: 2026-06-17T07:32:32.508Z,
  attachments: [
    {
      filename: 'notes.pdf',
      size_kb: 240
    }
  ]
}
{
  _id: ObjectId('6a324d90412a847f96907126'),
  student_id: 6,
  course_code: 'CS103',
  semester: '2022-ODD',
  rating: 5,
  comments: 'Excellent',
  tags: [
    'good-examples'
  ],
  submitted_at: 2026-06-17T07:32:32.508Z
}
{
  _id: ObjectId('6a324d90412a847f96907128'),
  student_id: 8,
  course_code: 'CS105',
  semester: '2022-ODD',
  rating: 5,
  comments: 'Outstanding',
  tags: [
    'challenging'
  ],
  submitted_at: 2026-06-17T07:32:32.508Z
}
db.feedback.find({
course_code:"CS101",
tags:"challenging"
})
{
  _id: ObjectId('6a324d90412a847f96907121'),
  student_id: 1,
  course_code: 'CS101',
  semester: '2022-ODD',
  rating: 5,
  comments: 'Excellent teaching',
  tags: [
    'challenging',
    'well-structured',
    'good-examples'
  ],
  submitted_at: 2026-06-17T07:32:32.508Z,
  attachments: [
    {
      filename: 'notes.pdf',
      size_kb: 240
    }
  ]
}
{
  _id: ObjectId('6a324d90412a847f96907122'),
  student_id: 2,
  course_code: 'CS101',
  semester: '2022-ODD',
  rating: 4,
  comments: 'Very good course',
  tags: [
    'challenging',
    'good-examples'
  ],
  submitted_at: 2026-06-17T07:32:32.508Z,
  attachments: [
    {
      filename: 'lab.pdf',
      size_kb: 120
    }
  ]
}
 
db.feedback.updateMany(
{needs_review:true},
{$push:{tags:"reviewed"}}
)
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 0,
  modifiedCount: 0,
  upsertedCount: 0
}
db.feedback.aggregate([
{
  $match:{
    semester:"2022-ODD"
  }
},
{
  $group:{
    _id:"$course_code",
    avg_rating:{$avg:"$rating"},
    feedback_count:{$sum:1}
  }
},
{
  $project:{
    _id:0,
    course_code:"$_id",
    average_rating:{
      $round:["$avg_rating",1]
    },
    feedback_count:1
  }
},
{
  $sort:{
    average_rating:-1
  }
}
])
{
  feedback_count: 1,
  course_code: 'CS103',
  average_rating: 5
}
{
  feedback_count: 1,
  course_code: 'CS105',
  average_rating: 5
}
{
  feedback_count: 3,
  course_code: 'CS101',
  average_rating: 4
}
{
  feedback_count: 1,
  course_code: 'CS107',
  average_rating: 4
}
{
  feedback_count: 1,
  course_code: 'CS106',
  average_rating: 3
}
{
  feedback_count: 2,
  course_code: 'CS102',
  average_rating: 1.5
}
db.feedback.aggregate([
{
  $unwind:"$tags"
},
{
  $group:{
    _id:"$tags",
    count:{$sum:1}
  }
},
{
  $sort:{
    count:-1
  }
}
])
{
  _id: 'good-examples',
  count: 4
}
{
  _id: 'well-structured',
  count: 3
}
{
  _id: 'challenging',
  count: 3
}
{
  _id: 'difficult',
  count: 1
}
{
  _id: 'confusing',
  count: 1
}
{
  _id: 'interactive',
  count: 1
}
college_nosql


