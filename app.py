import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── Page config ───────────────────────────────────────────────
st.set_page_config(
    page_title="Parcl Buyer Intelligence",
    page_icon="🏢",
    layout="wide"
)

# ── Load data ─────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("data/clients_clustered.csv")
    df['date_of_birth_std'] = df['date_of_birth'].str.replace('/', '-', regex=False)
    df['age'] = pd.to_datetime('today').year - pd.to_datetime(
        df['date_of_birth_std'], format='mixed', dayfirst=False).dt.year
    return df

df = load_data()

# ── Sidebar filters ───────────────────────────────────────────
st.sidebar.image("https://via.placeholder.com/200x60?text=Parcl+AI", width=200)
st.sidebar.title("Filters")

countries   = st.sidebar.multiselect("Country",
                sorted(df['country'].unique()),
                default=sorted(df['country'].unique()))
segments    = st.sidebar.multiselect("Segment",
                sorted(df['segment'].unique()),
                default=sorted(df['segment'].unique()))
client_type = st.sidebar.multiselect("Client type",
                sorted(df['client_type'].unique()),
                default=sorted(df['client_type'].unique()))
purpose     = st.sidebar.multiselect("Acquisition purpose",
                sorted(df['acquisition_purpose'].unique()),
                default=sorted(df['acquisition_purpose'].unique()))

filtered = df[
    df['country'].isin(countries) &
    df['segment'].isin(segments) &
    df['client_type'].isin(client_type) &
    df['acquisition_purpose'].isin(purpose)
]

# ── Header ────────────────────────────────────────────────────
st.title("🏢 Parcl — AI Buyer Intelligence Dashboard")
st.markdown("Machine learning based buyer segmentation and investment profiling")
st.divider()

# ── Module 1: KPI row ─────────────────────────────────────────
st.subheader("Overview")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total clients",      f"{len(filtered):,}")
c2.metric("Segments",           filtered['segment'].nunique())
c3.metric("Avg satisfaction",   f"{filtered['satisfaction_score'].mean():.2f}")
c4.metric("Investment buyers",  f"{(filtered['acquisition_purpose']=='Investment').mean()*100:.1f}%")
c5.metric("Loan applied",       f"{(filtered['loan_applied']=='Yes').mean()*100:.1f}%")
st.divider()

# ── Module 2: Buyer segmentation ──────────────────────────────
st.subheader("Module 1 — Buyer segmentation overview")
col1, col2 = st.columns(2)

with col1:
    fig_pie = px.pie(filtered, names='segment', title='Segment distribution',
        color='segment',
        color_discrete_map={
            'Corporate Buyers':  '#1D9E75',
            'First-Time Buyers': '#378ADD',
            'Global Investors':  '#D85A30',
            'Luxury Investors':  '#7F77DD'
        })
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    seg_count = filtered['segment'].value_counts().reset_index()
    seg_count.columns = ['segment', 'count']
    fig_bar = px.bar(seg_count, x='segment', y='count',
        title='Client count per segment',
        color='segment',
        color_discrete_map={
            'Corporate Buyers':  '#1D9E75',
            'First-Time Buyers': '#378ADD',
            'Global Investors':  '#D85A30',
            'Luxury Investors':  '#7F77DD'
        })
    fig_bar.update_layout(showlegend=False, xaxis_tickangle=-20)
    st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

# ── Module 3: Investor behavior ───────────────────────────────
st.subheader("Module 2 — Investor behavior dashboard")
col3, col4 = st.columns(2)

with col3:
    behavior = filtered.groupby('segment').agg(
        pct_investment = ('acquisition_purpose', lambda x: (x=='Investment').mean()*100),
        pct_loan       = ('loan_applied',        lambda x: (x=='Yes').mean()*100),
        avg_sat        = ('satisfaction_score',   'mean')
    ).reset_index().round(1)

    fig_beh = go.Figure()
    fig_beh.add_trace(go.Bar(name='Investment %', x=behavior['segment'], y=behavior['pct_investment'], marker_color='#D85A30'))
    fig_beh.add_trace(go.Bar(name='Loan %',       x=behavior['segment'], y=behavior['pct_loan'],       marker_color='#378ADD'))
    fig_beh.update_layout(barmode='group', title='Investment vs loan behavior by segment',
                          xaxis_tickangle=-20)
    st.plotly_chart(fig_beh, use_container_width=True)

with col4:
    fig_sat = px.box(filtered, x='segment', y='satisfaction_score',
        color='segment', title='Satisfaction score distribution',
        color_discrete_map={
            'Corporate Buyers':  '#1D9E75',
            'First-Time Buyers': '#378ADD',
            'Global Investors':  '#D85A30',
            'Luxury Investors':  '#7F77DD'
        })
    fig_sat.update_layout(showlegend=False, xaxis_tickangle=-20)
    st.plotly_chart(fig_sat, use_container_width=True)

st.divider()

# ── Module 4: Geographic analysis ────────────────────────────
st.subheader("Module 3 — Geographic buyer analysis")
col5, col6 = st.columns(2)

with col5:
    top_regions = filtered['region'].value_counts().head(12).index
    reg_df = filtered[filtered['region'].isin(top_regions)]
    reg_seg = reg_df.groupby(['region','segment']).size().reset_index(name='count')
    fig_reg = px.bar(reg_seg, x='region', y='count', color='segment',
        title='Segments by top regions',
        color_discrete_map={
            'Corporate Buyers':  '#1D9E75',
            'First-Time Buyers': '#378ADD',
            'Global Investors':  '#D85A30',
            'Luxury Investors':  '#7F77DD'
        })
    fig_reg.update_layout(xaxis_tickangle=-30)
    st.plotly_chart(fig_reg, use_container_width=True)

with col6:
    top_countries = filtered['country'].value_counts().head(10).index
    cnt_df = filtered[filtered['country'].isin(top_countries)]
    cnt_seg = cnt_df.groupby(['country','segment']).size().reset_index(name='count')
    fig_cnt = px.bar(cnt_seg, x='country', y='count', color='segment',
        title='Segments by country',
        color_discrete_map={
            'Corporate Buyers':  '#1D9E75',
            'First-Time Buyers': '#378ADD',
            'Global Investors':  '#D85A30',
            'Luxury Investors':  '#7F77DD'
        })
    fig_cnt.update_layout(xaxis_tickangle=-30)
    st.plotly_chart(fig_cnt, use_container_width=True)

st.divider()

# ── Module 5: Segment insights panel ─────────────────────────
st.subheader("Module 4 — Segment insights panel")
selected_seg = st.selectbox("Select a segment to inspect", sorted(df['segment'].unique()))
seg_df = filtered[filtered['segment'] == selected_seg]

s1, s2, s3, s4 = st.columns(4)
s1.metric("Clients in segment",  f"{len(seg_df):,}")
s2.metric("Avg age",             f"{seg_df['age'].mean():.1f} yrs")
s3.metric("Avg satisfaction",    f"{seg_df['satisfaction_score'].mean():.2f}")
s4.metric("Top country",         seg_df['country'].value_counts().index[0] if len(seg_df)>0 else "N/A")

col7, col8 = st.columns(2)
with col7:
    fig_ref = px.pie(seg_df, names='referral_channel',
        title=f'{selected_seg} — referral channels')
    st.plotly_chart(fig_ref, use_container_width=True)
with col8:
    fig_age = px.histogram(seg_df, x='age', nbins=20,
        title=f'{selected_seg} — age distribution',
        color_discrete_sequence=['#7F77DD'])
    st.plotly_chart(fig_age, use_container_width=True)

st.divider()
st.caption("Parcl × Unified Mentor | ML-based Buyer Segmentation | 2026")
