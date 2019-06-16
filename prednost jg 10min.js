db.getCollection('everything').aggregate([
    {
        $match: {
            'year': 2018
        }
    },
    {
        $addFields: {
            'blueJgAdv': { $subtract: [{ $arrayElemAt: ["$gold.blueJG", 10] }, { $arrayElemAt: ["$gold.redJG", 10]}] },
            'redJgAdv': { $subtract: [{ $arrayElemAt: ["$gold.redJG", 10]}, { $arrayElemAt: ["$gold.blueJG", 10] }] }
        }
    },
    {
        $project: {
            jg_array: [
                {
                    'gold_difference': '$blueJgAdv',
                    'winning_side': '$winningSide',
                    'side': 'blue'
                },
                {
                    'gold_difference': '$redJgAdv',
                    'winning_side': '$winningSide',
                    'side': 'red'
                }
            ]
        }
    },
    {
        $unwind: "$jg_array"
    },
    {
        $match: {
            $expr: {$and: [{$eq: [ "$jg_array.winning_side" , "$jg_array.side"]}, { $gt: ["$jg_array.gold_difference", 0]}]}
        }
    },
    {
        $group: { _id: 0, "count": { $sum: 1 }}
    },
    {
        $project: {
            "percentage": { $divide: ["$count", db.everything.find({ "year": 2018 }).count()] }
        }
    }
])
