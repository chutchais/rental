'use strict';


// .controller('Controller', ['$scope','$resource','Family',function($scope,$resource,Family) {

angular.module('rentalList').
    component('rentalList', {
        templateUrl: 'api/templates/rental-list.html',
        controller:['Rental','$cookies', '$location', '$routeParams', '$rootScope', '$scope','$resource', 
        function(Rental,$cookies, $location, $routeParams, $rootScope, $scope,$resource){
            // var family = $routeParams.model
            // var station = $routeParams.station
            // var range = $routeParams.range
            // $scope.model=family
            // $scope.showDateRange=false
            console.log('On Rental function')
            $scope.range = 'Equipment Rental Report'
            // $scope.dt = new Date();

            // $scope.$watch('txtsearch',function(){
            //     var xx = $scope.txtsearch
            //     if (xx.length > 2){
            //         console.log($scope.txtsearch)
            //     }
                
            // });
            var rental_kwrg = {"f":"2017-09-20" ,"t":"2017-09-22"}
            $scope.$watch('txtsearch', function (newValue, oldValue, scope) {
                //Do anything with $scope.letters
                
                var xx = $scope.txtsearch
                // console.log(newValue)
                if (xx.length > 2){
                    // console.log($scope.txtsearch)
                    // console.log(newValue + ' --Old:' + oldValue )
                    var rental_kwrg = {"q": newValue }
                        Rental.get(rental_kwrg,function(rentals) {
                            $scope.rentals = rentals
                            $scope.result = 'Found ' + rentals.length + ' record(s)'
                            }
                    );
                }
                else {
                    if ($scope.txtsearch == ''){
                    var rental_kwrg = {"f":"2017-09-20" ,"t":"2017-09-22"}
                    // console.log(rental_kwrg)
                    Rental.get(rental_kwrg,function(rentals) {
                            $scope.rentals = rentals
                            $scope.result = 'Total ' + rentals.length + ' record(s)'
                            }
                    );
                    }
                }
            });

            // $scope.$watch(function(scope) { return scope.txtsearch },
            //   function() {}
            //  );

            
            Rental.get(rental_kwrg,function(rentals) {
                    //do something with rental
                    console.log(rental_kwrg)
                    $scope.rentals = rentals
                    angular.forEach(rentals, function(rental) {
                       if (true){
                            // console.log(rental.name + '  ' + rental.start_date);
                          }
                    });
                });

        }]
    });