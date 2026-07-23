'''
use college_nosql

db.feedback.find({rating:5})

db.feedback.find({course_code:"CS101"})

db.feedback.updateMany({rating:{$lt:3}},{$set:{needs_review:true}})

db.feedback.find({needs_review:true})

db.feedback.createIndex({course_code:1})

db.feedback.getIndexes()

db.feedback.aggregate([
{$group:{_id:"$course_code",average_rating:{$avg:"$rating"},total_feedback:{$sum:1}}}
]) 
'''