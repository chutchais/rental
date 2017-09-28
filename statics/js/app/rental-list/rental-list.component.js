'use strict';


// .controller('Controller', ['$scope','$resource','Family',function($scope,$resource,Family) {

angular.module('rentalList').
    component('rentalList', {
        templateUrl: 'api/templates/rental-list.html',
        controller:['$cookies', '$location', '$routeParams', '$rootScope', '$scope','$resource', 
        function($cookies, $location, $routeParams, $rootScope, $scope,$resource){
            // var family = $routeParams.model
            // var station = $routeParams.station
            // var range = $routeParams.range
            // $scope.model=family
            // $scope.showDateRange=false
            console.log('On Rental function')
            $scope.range = '7day'

        }]
    });