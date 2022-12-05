
def get_location():
    applied_job = {
        'job_locations': [
          {
          'location_id': '9256',
          'city': 'Nacogdochessdsds',
          'state': 'Texas',
          'state_abbr': 'TX',
          'country': 'United States',
          'country_abbr': 'US',
          'lat_lon': {'lat': '31.603945500000', 'lon': '-94.656004000000'},
          'text': 'Nacogdoches, TX, 75964, USA',
          'parsed_text': 'Nacogdoches, TX, United States',
          'location_neutral': False
        },
          {
          'location_id': '9256',
          'city': 'Nacogdoches',
          'state': 'Texas',
          'state_abbr': 'TX',
          'country': 'United States',
          'country_abbr': 'US',
          'lat_lon': {'lat': '31.603945500000', 'lon': '-94.656004000000'},
          'text': 'Nacogdoches, TX, 75964, USA',
          'parsed_text': 'remote',
          'location_neutral': False
        }],
    }
    job_search = {
      'job_locations': ['Nacogdoches, TX'],
      'is_remote_work': True,
      'remote_works': ["Reomte"],
    }
    job_locations = applied_job.get("job_locations", [])
    apply_source = 2
    output = job_locations[0] if job_locations else {}

    candidate_search_location = job_search.get("job_locations")[0] if job_search and job_search.get("job_locations") else ""
    if apply_source == 1 or len(job_locations) <= 1 or not candidate_search_location:
        return output
    candidate_search_location = remove_zip_code(candidate_search_location.lower().split(","))
    # check job search parameter -> pass
    is_candidate_search_job_remote = bool(job_search.get('is_remote_work') and job_search.get('remote_works'))
    best_match = {"value": None, "score": -1}
    candidate_search_location = " ".join(candidate_search_location)
    remote_parsed_text = "remote"
    for job_location in job_locations:
        if is_candidate_search_job_remote and job_location.get("parsed_text", "").lower() == remote_parsed_text:
            output = job_location
            best_match = {"value": None, "score": -1}
            break        
        match_score = get_score(candidate_search_location, job_location)
        if best_match.get("score") < match_score:
            best_match.update(value=job_location, score=match_score)
    if best_match.get("value"):
        output = best_match.get("value")        
    return output
            
    
def get_score(candidate_search_location, job_location):    
    check_cases = [
        ["city"],
        ["state"],
        ["state_abbr"],
        ["country"],
        ["country_abbr"],
        ["city", "state"],
        ["city", "state_abbr"],
        ["state", "country"],
        ["state", "country_abbr"],
        ["state_abbr", "country_abbr"],
        ["city", "state", "country"],
        ["city", "state_abbr", "country"],
        ["city", "state_abbr", "country_abbr"]
    ]
    no_match = 0
    for check_case in check_cases:
        location = [job_location.get(case_value, "").lower() for case_value in check_case]
        location = " ".join(location)
        if candidate_search_location.lower() == location.lower():
            return len(check_case)
    return no_match
  

def remove_zip_code(type_locations):
    return [item.strip() for item in type_locations if not item.strip().isnumeric()]

print(get_location())