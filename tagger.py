import subprocess

def rfttag(text):

    cmd = [r'C:\Users\Askinkaty\Downloads\RFTagger\RFTagger\run.bat']
    p = subprocess.Popen(
        cmd, cwd=r'C:\Users\Askinkaty\Downloads\RFTagger\RFTagger',
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    out, err = p.communicate(text.encode("utf-8"))

    result = [tuple([el.strip() for el in line.split('\t')])
              for line in out.decode('utf-8').split('\n')]

    #clean result from tuple without all three component: word form, tag, lemma
    for i in range(len(result) - 1, -1, -1):
        if len(result[i]) < 3:
            del result[i]
            continue
        s1 = result[i][0].replace('\\n', '')
        result[i] = (s1, result[i][1], result[i][2])

    result_sent = []
    sent = []
    for i in range(len(result)):
        sent.append(result[i])
        if result[i][1] == 'SENT' or result[i][0] == '...' or i == len(result) - 1:
            result_sent.append(sent)
            sent = []
    #print(result_sent)
    #print(result)
    # print(err.decode('866'))
    return result_sent
