"""Export reproducible commit evidence without claiming a final grading decision.

Run at the repository root: python verification/audit_commits.py --ref HEAD --output /path/to/audit.json
The snapshot ends at the resolved SHA; later commits are not silently included.
"""
import argparse
import json
import subprocess
from pathlib import Path

def git(*args):
    return subprocess.check_output(['git',*args],encoding='utf-8')

def audit(ref):
    final=git('rev-parse','--verify',ref+'^{commit}').strip()
    commits=git('rev-list','--reverse',final).splitlines()
    records=[]
    for sha in commits:
        subject=git('show','-s','--format=%s',sha).strip()
        parents=git('show','-s','--format=%P',sha).split()
        stats=git('show','--format=','--numstat','--no-renames',sha).splitlines()
        files=[line.split('\t',2)[2] for line in stats if len(line.split('\t',2))==3]
        additions=sum(int(line.split('\t')[0]) for line in stats if line.split('\t')[0].isdigit())
        deletions=sum(int(line.split('\t')[1]) for line in stats if len(line.split('\t'))>1 and line.split('\t')[1].isdigit())
        status='candidate';reason='Actual tracked changes; final rubric review required.'
        if not parents:
            status='excluded';reason='Initial theme ZIP registration mixed with setup; conservatively excluded.'
        elif not files:
            status='excluded';reason='No own file changes shown (empty or merge-only); excluded.'
        elif all(f.startswith(('public/','site/public/')) for f in files):
            status='excluded';reason='Generated build output only; excluded.'
        record={'sha':sha,'subject':subject,'file_count':len(files),'additions':additions,'deletions':deletions,'status':status,'reason':reason,'url':'https://github.com/kimsungwoon5056-beep/MyProfile/commit/'+sha}
        if parents:record['files']=files
        if sha.startswith('bf4d6d0'):
            record['review_note']='Attempted fixed-position CSS repair; browser recheck did not confirm resolution. Later removed after user feedback. Assess as actual debugging attempt, not a proven successful fix.'
        records.append(record)
    excluded=sum(r['status']=='excluded' for r in records)
    return {'final_sha':final,'initial_sha':commits[0],'initial_included':False,'total':len(records),'excluded':excluded,'candidates':len(records)-excluded,'grading_status':'Provisional evidence only: inspect linked diffs and rubric. Not a claim of 50 valid commits.','records':records}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ref',default='HEAD');parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();data=audit(args.ref)
    args.output.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:data[k] for k in ['final_sha','total','excluded','candidates']},ensure_ascii=False))
