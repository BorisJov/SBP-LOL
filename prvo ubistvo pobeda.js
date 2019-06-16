db.getCollection('everything').aggregate([
    {
        $match: {
            "year": 2018
        }
    },
    {
        $unwind: "$kills"  
    },
    {
        $group: {
            _id: "$kills.killer", "kill_count" { $sum: 1 }
        }
    },
    {
        $group: { _id: 0, "kill_count": { $max: "$kill_count" } }
    },
    {
        $project: {
            "percentage": { $divide: ["$count", db.everything.find({ "year": 2018 }).count()] }
        }
    }
])