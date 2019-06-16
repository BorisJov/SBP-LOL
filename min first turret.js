db.getCollection('everything').aggregate([
    {
        $project: {
            'ft_object': { $arrayElemAt: ['$structures', 0] }
        }
    },
    {
        $project: {
            'first_turret_lane': '$ft_object.lane',
            'first_turret': '$ft_object.type',
            'time': '$ft_object.time'
        }
    },
    {
        $group: { _id: 0, "minimumTime": { $min: '$time' } }
    },
    {
        $sort: { count: -1 }
    }
])