from pywps.Process import WPSProcess
class Process(WPSProcess):

  def __init__(self):
    ##
    # Process initialization
    WPSProcess.__init__(self,
        identifier = "word_counter",
        title="Word Counter",
        abstract="""Counts words in text document.""",
        )

    ##
    # Adding process inputs

    self.resource = self.addComplexInput(identifier="resource",
              title="Input Text Document",
              formats = [{'mimeType':'text/plain'}])


    ##
    # Adding process outputs

    self.output = self.addComplexOutput(identifier = "output",
            title="JSON Document with occurrences of Words")

    ##
    # Execution part of the process
    def execute(self):

        # count words and save result
        self.output.setValue( count_words( self.resource.getValue() )  )

        return
