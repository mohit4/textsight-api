"""

basic_analysis.py

Contains utility methods to interact with text using TextBlob and perform text processing.
Not quite powerful but effective :)

"""

__author__ = "Mohit Kumar"
__copyright__ = "Copyright 2021, textsight-api"
__credits__ = ["Mohit Kumar"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Mohit Kumar"
__email__ = "mohitkumar2801@gmail.com"
__status__ = "Development"

from textblob import TextBlob

def _getPolarityFromScore( polarity_score ):
    """
    Accepts the polarity score and returns the label

    -1.00 to -0.90 - Very Negative
    -0.90 to -0.10 - Negative
    -0.10 to  0.10 - Neutral
     0.10 to  0.90 - Positive
     0.90 to  1.00 - Very Positive

    """

    status = "unknown"

    if  ( -1.00 <= polarity_score <= -0.90 ): 
        return "Very Negative"
    elif( -0.90 <  polarity_score <  -0.10 ):
        return "Negative"
    elif( -0.10 <= polarity_score <=  0.10 ):
        return "Neutral"
    elif(  0.10 <  polarity_score <   0.90 ):
        return "Positive"
    elif(  0.90 <= polarity_score <=  1.00 ):
        return "Very Positive"

    return status

def _getSubjectivityFromScore( polarity_score ):
    """
    Accepts the subjectivity score and returns the label

     0.00 to 0.10 - Very Objective
     0.10 to 0.45 - Objective
     0.45 to 0.55 - Neutral
     0.55 to 0.90 - Subjective
     0.90 to 1.00 - Very Subjective

    """

    status = "unknown"

    if  ( 0.00 <= polarity_score <= 0.10 ): 
        return "Very Objective"
    elif( 0.10 <  polarity_score <  0.45 ):
        return "Objective"
    elif( 0.45 <= polarity_score <= 0.55 ):
        return "Neutral"
    elif( 0.55 <  polarity_score <  0.90 ):
        return "Subjective"
    elif( 0.90 <= polarity_score <= 1.00 ):
        return "Very Subjective"

    return status

def getBasicAnalysisData( text ):
    """Accepts text and provided basic text processing data"""
    tb = TextBlob( text )

    polarity_score = tb.polarity
    polarity       = _getPolarityFromScore( polarity_score )
    
    subjectivity_score = tb.subjectivity
    subjectivity       = _getSubjectivityFromScore( subjectivity_score )
    
    tags = list( tb.noun_phrases )

    basic_processed_data = {
        "polarity_score": polarity_score,
        "polarity": polarity,
        "subjectivity_score": subjectivity_score,
        "subjectivity": subjectivity,
        "tags": tags 
    }

    return basic_processed_data