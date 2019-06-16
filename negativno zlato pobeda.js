db.getCollection('everything').aggregate([
    {
        $match: {
            'year': 2018
        }
    },
    {
        $project: {
            'winning_side': '$winningSide',
            'end_gold_difference': { $arrayElemAt: ["$gold.difference", -1]}
        }
    },
    {
        $project: {
            winning_side: 1,
            gold_adv_side: {
                $cond: {
                    if: { $gte: [ '$end_gold_difference', 0] },
                    then: "blue",
                    else: 'red'
                
                }
            }
        }
    },
    {
        $match: {
            $expr: { $ne: ["$winning_side", "$gold_adv_side"] }
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