from pywps.Process import WPSProcess
class Process(WPSProcess):

  def __init__(self):
    ##
    # Process initialization
    WPSProcess.__init__(self,
        identifier = "wordcount",
        title="Word Counter",
        abstract="""Counts words in text document.""",
        )

    ##
    # Adding process inputs

    self.text = self.addComplexInput(identifier="text",
              title="Text Document",
              formats = [{'mimeType':'text/plain'}])


    ##
    # Adding process outputs

    self.output = self.addComplexOutput(identifier = "output",
            title="Word count result")

    ##
    # Execution part of the process
    def execute(self):

        # count words and save result
        self.output.setValue( count_words( self.text.getValue() )  )

        return
