import geb.spock.GebReportingSpec
import pages.app.RegisterPage
import spock.lang.*

class SearchRegistrySpecs extends GebReportingSpec {

    @Unroll
    def "Search Registry: #TestDesc"(){
       	given: "that I am an general user"
           to RegisterPage
        when: "I search for a registered driller/installer"
            at RegisterPage
            reset
            if ( "$SearchType" == "community") {
                selectcommunity = ["$Search"]
            }    
            if ( "$SearchType" == "installer") {
                selectinstaller
            } else {
                selectdriller
            }
            if ( "$SearchType" == "name") {
                search.value("$Search")
            }    
            submit
        then: "I should find the result"
            if ( "$NumberResult" == "none" ) {
                assert waitFor { noresults.displayed }
            } else {
                assert waitFor { result == "$NumberResult" }
            }

        where:
        TestDesc 					| Search          	| SearchType      | Results             | NumberResult
        "Empty search criteria"     | ""			    | ""              | ""				    | "65"
        "Empty search criteria - Driller"     | ""			    | "driller"       | ""				    | "65"
        "Empty search criteria - Installer"     | ""			    | "installer"       | ""				    | "none"
        "Name=John"                 | "John"			| "name"          | ""				    | "1"
        "Name=Alan"                 | "Alan"			| "name"          | ""				    | "2"
        "Community=Langley"                 | "Langley"			| "community"          | ""				    | "1"
        "Community=Langley and Aldergrove"                 | "Aldergrove"			| "community"          | ""				    | "2"
    }
}
