db.getCollection('everything').aggregate([
    {
        $match: {
            'year': 2018
        }
    },
    {
        $addFields: {
            'end_gold_difference': { $arrayElemAt: ["$gold.difference", -1]}
        }
    },
    {
        $addFields: {
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
            $expr: { $ne: [ "$winningSide" , "$gold_adv_side"] }
        }
    },
    {
        $group: {
            _id: 0,
            address: { $first: "$address" },
            blueTeam: { $first: "$blueTeam.blueTeamTag" },
            redTeam: { $first: "$redTeam.redTeamTag" },
            winningSide: { $first: "$winningSide" },
            goldDifference: { $first: "$end_gold_difference" },
            "minimum" : { $max: { $abs: "$end_gold_difference"} }
        }
    }
])