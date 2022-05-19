var map = function () {
    var simpledate = this.date;

    simpledate.setSeconds(0);
    simpledate.setHours(0);
    simpledate.setMinutes(0);
    simpledate.setMilliseconds(0);

    emit(simpledate, this.totalAmount)
};

var reduce = function(date, totalAmount) {
    return Array.sum(totalAmount);
};

db.SGD.orders.mapReduce(map, reduce, {out: {inline: 1}});
