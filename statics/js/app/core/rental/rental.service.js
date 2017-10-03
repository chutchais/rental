'use strict';

angular.
    module('rental').
        factory('Rental', function($resource){
            // return 'hello Family'
            // console.log('Family function execute')
            var url = '/api/rental/'
            //console.log($resource)
            return $resource(url, {}, {
                "query": {
                    method: "GET",
                    params: {},
                    isArray: true,
                    cache: false,
                    transformResponse: function(data, headersGetter, status){
                        var finalData = angular.fromJson(data)
                        return finalData
                        //finalData.results
                    }
                    // interceptor
                },
                "get": {
                    method: "GET",
                    // params: {"slug": "@slug"},
                    params: {},
                    isArray: true,
                    cache: false,
                    transformResponse: function(data, headersGetter, status){
                        var finalData = angular.fromJson(data)
                        return finalData
                        //finalData.results
                    }
                },
            })
            
        });