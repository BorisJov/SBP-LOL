db.getCollection('everything').aggregate([
    {
        $match: {
            "year": 2017
        }
    },
    {
        $unwind: "$kills"  
    },
    {
        $group: {
            _id: "$kills.killer", "name": { $first: "$kills.killer"}, "kill_count": { $sum: 1 }
        }
    },
    {
        $sort: {kill_count:-1}
    },
    {
        $limit: 1
    }
])