db.getCollection('everything').aggregate([
    {
        $match: {
            'year': 2018
        }
    },
    {
        $project: {
            'winning_side': '$winningSide',
            'herald_array': '$neutral_objectives.heralds'
        }
    },
    {
        $match: {
            $expr: { $gte: [ {$size: "$herald_array"}, 0] }
        }
    },
    {
        $project: {
            winning_side: 1, 
            'herald_obj': { $arrayElemAt: ["$herald_array", 0] }
        }
    },
    {
        $project: {
            winning_side: 1, 
            'herald_side': '$herald_obj.side'
        }
    },
    {
        $match: {
            $expr: { $eq: ["$winning_side", "$herald_side"] }
        }
    },
    {
        $group: { _id: 0, "count": { $sum: 1 } }
    },
    {
        $project: {
            "percentage": { $divide: ["$count", db.everything.find({ "year": 2018 }).count()] }
        }
    }
])