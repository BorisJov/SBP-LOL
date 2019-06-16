db.getCollection('everything').aggregate([
    {
        $match: {
            "year": 2018
        }
    },
    {
        $project: {
            'ft_object': { $arrayElemAt: ['$structures', 0] }
        }
    },
    {
        $project: {
            'first_turret_lane': '$ft_object.lane',
            'first_turret': '$ft_object.type'
        }
    },
    {
        $group: { _id: { 'first_turret_lane': '$first_turret_lane', 'first_turret_type': '$first_turret_type' }, "count": { $sum: 1 } }
    },
    {
        $sort: { count: -1 }
    }
])