db.getCollection('everything').aggregate([
    {
      $match: {
          "year": 2018
      }  
    },
    {
        $project: {
            winningSide: 1
        }
    },
    {
        $group: { _id: "$winningSide", "count": { $sum: 1 } }
    }
])