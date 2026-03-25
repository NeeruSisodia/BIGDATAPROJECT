# MongoDB Schema Design
## Project: Airline Tweet Sentiment Analysis

---

## Database Information

| Detail | Value |
|--------|-------|
| **Database Name** | tweets_db |
| **Collection Name** | airline_tweets |
| **Total Documents** | 14,478 |
| **Storage Engine** | WiredTiger (MongoDB default) |

---

## Document Structure
```json
{
  "_id": ObjectId("auto-generated"),
  "tweet_id": "570306133677760513",
  "airline_sentiment": "neutral",
  "airline_sentiment_confidence": 1.0,
  "negativereason": null,
  "airline": "Virgin America",
  "retweet_count": 0,
  "text": "@VirginAmerica What @dhepburn said.",
  "clean_text": "what said",
  "tweet_created": "2015-02-24 11:35:52 -0800",
  "tweet_location": "Los Angeles"
}
```

---

## Field Definitions

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| _id | ObjectId | No | Auto-generated MongoDB unique ID |
| tweet_id | String | No | Unique Twitter tweet identifier |
| airline_sentiment | String | No | Sentiment: positive / neutral / negative |
| airline_sentiment_confidence | Float | Yes | Confidence score 0.0 to 1.0 |
| negativereason | String | Yes | Reason for negative tweet (null if not negative) |
| airline | String | No | Airline name mentioned in tweet |
| retweet_count | Integer | Yes | Number of retweets |
| text | String | No | Original raw tweet text |
| clean_text | String | No | Cleaned tweet text (processed) |
| tweet_created | String | Yes | Tweet creation timestamp |
| tweet_location | String | Yes | User location if provided |

---

## Allowed Field Values

### airline_sentiment
- positive — tweet expresses satisfaction
- neutral  — tweet is neither positive nor negative
- negative — tweet expresses a complaint

### airline
- United
- US Airways
- American
- Southwest
- Delta
- Virgin America

### negativereason
- Customer Service Issue
- Late Flight
- Can't Tell
- Cancelled Flight
- Lost Luggage
- Bad Flight
- Flight Booking Problems
- Flight Attendant Complaints
- longlines
- Damaged Luggage

---

## Indexes

### Index 1 — Airline
```python
collection.create_index("airline")
```
- Type: Single field ascending
- Purpose: Fast filtering by airline name

### Index 2 — Sentiment
```python
collection.create_index("airline_sentiment")
```
- Type: Single field ascending
- Purpose: Fast sentiment-based queries

### Index 3 — Negative Reason
```python
collection.create_index("negativereason")
```
- Type: Single field ascending
- Purpose: Fast complaint reason lookups

### Index 4 — Tweet ID
```python
collection.create_index("tweet_id", unique=False)
```
- Type: Single field ascending
- Purpose: Fast lookup by tweet ID

### Index 5 — Compound (Airline + Sentiment)
```python
collection.create_index([("airline", 1), ("airline_sentiment", 1)])
```
- Type: Compound index
- Purpose: Optimized queries filtering by both airline AND sentiment together

---

## Sample Aggregation Queries

### Count by Sentiment
```javascript
db.airline_tweets.aggregate([
  { "$group": { "_id": "$airline_sentiment", "count": { "$sum": 1 } } },
  { "$sort": { "count": -1 } }
])
```
Result:
- negative → 9110
- neutral  → 3069
- positive → 2299

### Top Negative Reasons
```javascript
db.airline_tweets.aggregate([
  { "$match": { "airline_sentiment": "negative" } },
  { "$group": { "_id": "$negativereason", "count": { "$sum": 1 } } },
  { "$sort": { "count": -1 } },
  { "$limit": 5 }
])
```
Result:
- Customer Service Issue → 2883
- Late Flight            → 1648
- Can't Tell             → 1175
- Cancelled Flight       → 829
- Lost Luggage           → 717

### Worst Airline
```javascript
db.airline_tweets.aggregate([
  { "$match": { "airline_sentiment": "negative" } },
  { "$group": { "_id": "$airline", "count": { "$sum": 1 } } },
  { "$sort": { "count": -1 } },
  { "$limit": 1 }
])
```
Result: United → 2630 complaints

### Best Airline
```javascript
db.airline_tweets.aggregate([
  { "$match": { "airline_sentiment": "positive" } },
  { "$group": { "_id": "$airline", "count": { "$sum": 1 } } },
  { "$sort": { "count": -1 } },
  { "$limit": 1 }
])
```
Result: Southwest → 570 positive tweets

---

## Performance Results

| Query | Without Index | With Index |
|-------|--------------|------------|
| Filter by airline | ~0.15 sec | ~0.02 sec |
| Filter by sentiment | ~0.12 sec | ~0.07 sec |
| Compound filter | ~0.18 sec | ~0.03 sec |

---

## Schema Design Decisions

- MongoDB chosen because tweet data is semi-structured
- Missing fields handled naturally without NULL constraints
- Single collection used — no joins needed
- Compound index covers most common query pattern
- unique=False on tweet_id avoids DuplicateKeyError from dataset duplicates



