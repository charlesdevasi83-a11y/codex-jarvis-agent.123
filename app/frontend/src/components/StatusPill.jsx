export default function StatusPill({ label, healthy }) {
  return (
    <span className={`status-pill ${healthy ? 'healthy' : 'warning'}`}>
      {healthy ? '●' : '○'} {label}
    </span>
  )
}
