db.getCollection('everything').aggregate([
    {
      $match: {
          "year": 2017
      }  
    },
    {
        $project: {
            "winner": {
                $cond: {
                    if: { $eq: ["$winningSide", 'blue'] },
                    then: "$blueTeam.blueTeamTag",
                    else: "$redTeam.redTeamTag"
                }
            }
        }
    },
    {
        $group: { _id: "$winner", "count": { $sum: 1 } }
    },
    { 
        $sort: { count: -1 }
    },
    {
        $limit: 1
    }
])