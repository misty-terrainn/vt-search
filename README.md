# VT Search

## Description
A Python3 tool for fetching VirusTotal Intelligence Search results programmatically.  
This tool wraps the multiple requests needed to fetch anything exceeding 300 results.  
Currently, the tool only fetches sample metadata and does not download the actual samples (to do?).  
Output is written to JSON files in ./output.  

Reference: <https://developers.virustotal.com/reference/intelligence-search>

## Configuration
Add a VirusTotal Enterprise API key to config.ini before using the script.  
(Check with me if you want a key!)

## Example usage

You can provide a query string, using the same syntax as the VirusTotal Intelligence web interface 
(refer [here](https://support.virustotal.com/hc/en-us/articles/360001385897-File-search-modifiers) for search modifiers). 

```
# Find samples with comments by user "thor", last submitted between 2022-04-04 and 2022-04-17
./vt_search.py -q "comment_author:thor ls:2022-04-04T00:00:00+ ls:2022-04-17T00:00:00-"

# Find samples submitted from SG, last submitted between 2022-04-01 and 2022-04-10
./vt_search.py -q "submitter:SG ls:2022-04-01+ ls:2022-04-10-"
```

Or you can directly provide a query URL, e.g. from an unfinished query recorded in the logs:
```
./vt_search.py -u "https://www.virustotal.com/api/v3/intelligence/search?cursor=eJwNyrEOgjAQANBfggIlDA7GUnLDXaMxaa6rJsq1nRyECx-vb36t7cdhtLabjqizIZe_JLyh4w9cYAiRcrq_lCUVkpKDO7dhue4h4oYV_p9WWrBnBcPGVxSqrLeMdd5R_YoKmuRZsHpJ8pbkHg2U5nT8ACP3KBI%3D&query=comment_author%3Athor+ls%3A2022-04-04%2B+ls%3A2022-04-17-&limit=300&order=last_submission_date+"
```

Check the help for more options:
```
./vt_search.py -h
```

## Notes
* VirusTotal only returns results within the last 90 days.
* Search tends to terminate early if the date range is too large.

## Scripts
* `scripts/tally_dates.py` — scans the output directory and lists the distinct dates (e.g. `last_submission_date`) covered by the collected results:
  ```
  ./scripts/tally_dates.py -d output -a last_submission_date
  ```

## Roadmap
* Nicer UI / refactor
* Download samples
* Fetch comments when `crowdsourced_yara` is not populated
