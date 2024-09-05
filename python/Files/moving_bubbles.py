from D3blocks import D3Blocks

d3 = D3blocks()

d3.movingbubbles(df,
                 datetime = "Timestamp",
                 sample_id = "Sample ID",
                 state = "Sample State",
                 filepath = "moving.html"
)