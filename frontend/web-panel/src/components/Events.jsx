import React, { useEffect, useState } from 'react';
import { api } from '../services/api';

export default function Events() {
  const [events, setEvents] = useState([]);
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [editId, setEditId] = useState(null);

  const load = async () => {
    const res = await api.get('/events');
    setEvents(res.data);
  };
  useEffect(() => { load(); }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (editId) {
      await api.put(`/events/${editId}`, { name, description });
    } else {
      await api.post('/events', { name, description });
    }
    setName(''); setDescription(''); setEditId(null);
    load();
  };

  const handleEdit = (event) => {
    setEditId(event.id);
    setName(event.name);
    setDescription(event.description || '');
  };

  const handleDelete = async (id) => {
    await api.delete(`/events/${id}`);
    load();
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold">Events</h2>
      <form onSubmit={handleSubmit} className="my-4">
        <input
          type="text" placeholder="Name"
          value={name} onChange={e => setName(e.target.value)}
          className="border p-2 mr-2"
          required />
        <input
          type="text" placeholder="Description"
          value={description} onChange={e => setDescription(e.target.value)}
          className="border p-2 mr-2" />
        <button type="submit" className="bg-blue-500 text-white p-2 rounded">
          {editId ? 'Update' : 'Create'}
        </button>
      </form>
      <ul>
        {events.map(evt => (
          <li key={evt.id} className="flex justify-between items-center mb-2">
            <div>
              <strong>{evt.name}</strong>: {evt.description}
            </div>
            <div>
              <button onClick={() => handleEdit(evt)} className="mr-2">Edit</button>
              <button onClick={() => handleDelete(evt.id)}>Delete</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
