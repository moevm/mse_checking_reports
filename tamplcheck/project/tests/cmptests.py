from project.module.cmpFiles import comparison_algorithm, analysis_doc


def test_compare():
    if comparison_algorithm(analysis_doc("test.docx"), analysis_doc("test.docx")) == []:
        print("files are equal")
    else:
        print("files are not equal")


def test_analysis():
    if analysis_doc("test.docx") != {}:
        print("test file parameter list is not null")
    else:
        print("test file parameter list is null")